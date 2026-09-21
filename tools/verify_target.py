#!/usr/bin/env python3
"""Verify a local GBA input against config/target.json without retaining bytes."""
from __future__ import annotations
import argparse,hashlib,json
from pathlib import Path

def inspect_bytes(data:bytes)->dict:
 if len(data)<0xC0:raise ValueError("input is too small for a GBA header")
 return {"size":len(data),"sha1":hashlib.sha1(data).hexdigest(),"sha256":hashlib.sha256(data).hexdigest(),"header":{"title":data[0xA0:0xAC].split(b"\0",1)[0].decode("ascii",errors="replace").rstrip(),"game_code":data[0xAC:0xB0].decode("ascii",errors="replace"),"maker_code":data[0xB0:0xB2].decode("ascii",errors="replace"),"software_version":data[0xBC],"header_checksum":data[0xBD],"calculated_header_checksum":(-sum(data[0xA0:0xBD])-0x19)&0xFF}}

def compare_identity(observed:dict,target:dict)->dict:
 expected_hashes={x["algorithm"].lower():x["value"].lower() for x in target["hashes"]}; expected_header=target["header"]
 checks={"size":observed["size"]==target["size"],"sha1":observed["sha1"]==expected_hashes.get("sha1"),"sha256":observed["sha256"]==expected_hashes.get("sha256"),"header_checksum_valid":observed["header"]["header_checksum"]==observed["header"]["calculated_header_checksum"]}
 for key in ("title","game_code","maker_code","software_version","header_checksum"):checks[f"header_{key}"]=observed["header"][key]==expected_header[key]
 return checks

def main()->int:
 p=argparse.ArgumentParser(description=__doc__);p.add_argument("input",type=Path);p.add_argument("--target",type=Path,default=Path("config/target.json"));p.add_argument("--compact",action="store_true");a=p.parse_args()
 target=json.loads(a.target.read_text(encoding="utf-8"));observed=inspect_bytes(a.input.read_bytes());checks=compare_identity(observed,target);result={"target":target["repository"],"identity_status":target["identity_status"],"observed":observed,"checks":checks,"matches":all(checks.values())};print(json.dumps(result,ensure_ascii=True,indent=None if a.compact else 2));return 0 if result["matches"] else 1
if __name__=="__main__":raise SystemExit(main())
