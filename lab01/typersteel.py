#!/usr/bin/env python3
import sys

name = "appsec world"
print("Hello " + name)

if len(sys.argv) > 1:
    user_name = sys.argv[1]
    print(f"Hello {name} from {user_name}")
else:
    print("No name provided")
