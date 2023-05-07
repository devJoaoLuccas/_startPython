import platform

# give me the platform i'm using to run my IDE

print(platform.platform(True))

# give me the generic name of the processor

print("\n", platform.machine())

# give me the REAL name of the processor

print("\n", platform.processor())

# give me the generic version of the system

print("\n", platform.system())

# give me the REAL version of the system

print("\n", platform.version())

# give me the Python implemation

print("\n", platform.python_implementation())

# give me the three-element-tuple filled

for i in platform.python_version_tuple():
    print(i)
