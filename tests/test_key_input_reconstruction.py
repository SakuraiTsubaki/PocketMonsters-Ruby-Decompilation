import hashlib,json,re,unittest
from pathlib import Path
ROOT=Path(__file__).parents[1]
class Tests(unittest.TestCase):
 def test_map_and_source(self):
  m=json.loads((ROOT/'analysis/ruby-jp-key-input-map.json').read_text());s=(ROOT/'src/key_input.c').read_text()
  self.assertEqual([f['address'] for f in m['functions']],[0x08000404,0x0800042C]);self.assertEqual(m['literal_addresses']['REG_KEYINPUT'],'0x04000130')
  for name in ('InitKeys','ReadKeys'): self.assertIn(name+'(',s)
  for token in ('gMain.keyRepeatCounter--','gMain.newKeys |= A_BUTTON','gMain.watchedKeysPressed = 1'): self.assertIn(token,s)
  self.assertFalse(m['naming_basis']['raw_rom_bytes_published'])
 def test_struct_offsets_are_documented(self):
  m=json.loads((ROOT/'analysis/ruby-jp-key-input-map.json').read_text());self.assertEqual(m['proven_offsets'],{'heldKeysRaw':40,'newKeysRaw':42,'heldKeys':44,'newKeys':46,'newAndRepeatedKeys':48,'keyRepeatCounter':50,'watchedKeysPressed':52,'watchedKeysMask':54,'optionsButtonMode':19})
 def test_publication_files_are_hashable(self):
  manifest=json.loads((ROOT/'manifests/key-input-reconstruction.json').read_text());self.assertFalse(manifest['raw_rom_bytes_included'])
  for output in manifest['outputs']: self.assertEqual(hashlib.sha256((ROOT/output['path']).read_bytes()).hexdigest(),output['sha256'])
if __name__=='__main__':unittest.main()
