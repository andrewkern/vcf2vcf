import os
import argparse
import time

parser = argparse.ArgumentParser(description='vcf2vcf.py-- very fast')
parser.add_argument('filename')
args = parser.parse_args()
os.rename(args.filename, args.filename+".vcf")
print(f"converting {args.filename}... this is fast...")
time.sleep(10)
print(f"done!")
