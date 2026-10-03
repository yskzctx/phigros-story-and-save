"""Verify public artifacts using only the Python standard library."""
from pathlib import Path
import argparse
import hashlib
import json
import re
import zipfile

ROOT = Path(__file__).resolve().parent.parent


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--artifacts-dir', type=Path, help='Check registered release assets present in this download directory')
    args = parser.parse_args()
    checked = 0
    for line in (ROOT / 'SHA256SUMS').read_text().splitlines():
        expected, name = line.split('  ', 1)
        path = (ROOT / name).resolve()
        assert path.is_relative_to(ROOT), 'Invalid manifest path'
        actual = hashlib.sha256(path.read_bytes()).hexdigest()
        assert actual == expected, f'Checksum mismatch: {name}'
        checked += 1

    items = json.loads((ROOT / 'data/collections.json').read_text())
    assert len(items) == 503
    assert len({item['id'] for item in items}) == 503
    assert all(item['game_location'] for item in items)

    report = json.loads((ROOT / 'verification/save.json').read_text())
    assert report['variant'] == 'anonymous-ap'
    assert report['all_ap_verified'] and report['all_collection_records_covered']
    assert report['runtime_tested'] is False
    assert report['regular_charts'] == 1037

    assets = json.loads((ROOT / 'verification/release-assets.json').read_text())['assets']
    assert len({item['name'] for item in assets}) == len(assets)
    assert all(Path(item['name']).name == item['name'] for item in assets)
    assert all(re.fullmatch('[a-f0-9]{64}', item['sha256']) for item in assets)
    artifact_count = 0
    if args.artifacts_dir:
        for item in assets:
            path = args.artifacts_dir / item['name']
            if not path.is_file():
                continue
            assert path.stat().st_size == item['bytes'], f'Size mismatch: {item["name"]}'
            assert hashlib.sha256(path.read_bytes()).hexdigest() == item['sha256'], f'Checksum mismatch: {item["name"]}'
            artifact_count += 1
            if path.suffix == '.zip':
                with zipfile.ZipFile(path) as archive:
                    assert archive.testzip() is None, f'Corrupt archive: {path.name}'
            if path.name == 'Phigros-4.0.1-157-AllAP-Android-Root.zip':
                check_save(path)
        assert artifact_count, 'No registered release assets found in the download directory'

    book = json.loads((ROOT / 'verification/book.json').read_text())
    assert book['items'] == 503 and book['broken_links'] == 0
    assert book['new_items_all_cited_in_narrative']
    print(f'OK: {checked} source checksums, 503 collection locations, {len(assets)} release records, {artifact_count} downloaded assets.')


def check_save(path):
    with zipfile.ZipFile(path) as archive:
        expected_files = {'com.PigeonGames.Phigros.v2.playerprefs.xml', 'editable.decrypted.xml', 'verification.json', '收藏品清单.json', '使用说明.txt'}
        assert set(archive.namelist()) == expected_files
        report = json.loads(archive.read('verification.json'))
        assert report['variant'] == 'anonymous-ap'
        assert report['all_ap_verified'] and report['all_collection_records_covered']
        assert report['runtime_tested'] is False
        assert report['regular_charts'] == 1037
        import xml.etree.ElementTree as ET
        ET.fromstring(archive.read('com.PigeonGames.Phigros.v2.playerprefs.xml'))
        plain = ET.fromstring(archive.read('editable.decrypted.xml'))
        names = [node.get('name', '') for node in plain]
        assert not any(name.startswith('unity.cloud') or name == 'unity.player_sessionid' for name in names)

if __name__ == '__main__':
    main()
