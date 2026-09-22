from __future__ import annotations
import importlib.util,unittest
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1];spec=importlib.util.spec_from_file_location("verify_target",ROOT/"tools"/"verify_target.py");mod=importlib.util.module_from_spec(spec);spec.loader.exec_module(mod)
def fixture():
 data=bytearray(0x200);data[0xA0:0xAC]=b"POKEMON RUBY";data[0xAC:0xB0]=b"AXVJ";data[0xB0:0xB2]=b"01";data[0xB2]=0x96;data[0xBC]=0;data[0xBD]=(-sum(data[0xA0:0xBD])-0x19)&0xFF;return bytes(data)
class VerifyTargetTests(unittest.TestCase):
 def test_matching_identity(self):
  o=mod.inspect_bytes(fixture());target={"size":len(fixture()),"hashes":[{"algorithm":"sha1","value":o["sha1"]},{"algorithm":"sha256","value":o["sha256"]}],"header":{"title":"POKEMON RUBY","game_code":"AXVJ","maker_code":"01","software_version":0,"header_checksum":o["header"]["header_checksum"]}};self.assertTrue(all(mod.compare_identity(o,target).values()))
 def test_wrong_revision_is_rejected(self):
  o=mod.inspect_bytes(fixture());target={"size":len(fixture()),"hashes":[{"algorithm":"sha1","value":o["sha1"]},{"algorithm":"sha256","value":o["sha256"]}],"header":{"title":"POKEMON RUBY","game_code":"AXVJ","maker_code":"01","software_version":1,"header_checksum":o["header"]["header_checksum"]}};self.assertFalse(mod.compare_identity(o,target)["header_software_version"])
 def test_short_input_is_rejected(self):
  with self.assertRaisesRegex(ValueError,"too small"):mod.inspect_bytes(bytes(0xBF))
if __name__=="__main__":unittest.main()
