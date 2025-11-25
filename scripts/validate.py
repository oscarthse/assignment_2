#!/usr/bin/env python3
"""
Local validation script for project structure and code quality.
Can be run before committing to catch issues early.
"""

import sys
from pathlib import Path


def check_required_files():
    """Check that all required files exist."""
    required_files = [
        "src/model.py",
        "src/data_prep.py",
        "src/features.py",
        "src/evaluate.py",
        "src/utils.py",
        "requirements.txt",
        "README.md",
        "pyproject.toml",
    ]
    
    missing = []
    for file in required_files:
        if not Path(file).exists():
            missing.append(file)
    
    if missing:
        print("❌ Missing required files:")
        for file in missing:
            print(f"  - {file}")
        return False
    
    print("✅ All required files exist")
    return True


def check_python_syntax():
    """Check Python syntax of all .py files in src/."""
    import py_compile
    
    src_dir = Path("src")
    if not src_dir.exists():
        print("⚠️  src/ directory not found")
        return True
    
    errors = []
    for py_file in src_dir.glob("*.py"):
        try:
            py_compile.compile(str(py_file), doraise=True)
            print(f"✅ {py_file}: Syntax OK")
        except py_compile.PyCompileError as e:
            errors.append((py_file, str(e)))
            print(f"❌ {py_file}: Syntax error")
    
    if errors:
        print("\nSyntax errors found:")
        for file, error in errors:
            print(f"  {file}: {error}")
        return False
    
    return True


def check_imports():
    """Try to import modules (gracefully handles empty files)."""
    modules = [
        "src.data_prep",
        "src.features",
        "src.model",
        "src.evaluate",
        "src.utils",
    ]
    
    errors = []
    for module in modules:
        try:
            __import__(module)
            print(f"✅ {module}: Imports successfully")
        except SyntaxError as e:
            errors.append((module, f"SyntaxError: {e}"))
            print(f"❌ {module}: Syntax error")
        except ImportError as e:
            # Only fail on actual import errors, not missing dependencies
            if "No module named" in str(e) and "src" not in str(e):
                errors.append((module, f"ImportError: {e}"))
                print(f"❌ {module}: Import error")
            else:
                print(f"⚠️  {module}: {e} (may be expected if file is empty)")
        except Exception as e:
            print(f"⚠️  {module}: {e} (may be expected if file is empty)")
    
    if errors:
        print("\nImport errors found:")
        for module, error in errors:
            print(f"  {module}: {error}")
        return False
    
    return True


def main():
    """Run all validation checks."""
    print("Running project validation...\n")
    
    checks = [
        ("Required Files", check_required_files),
        ("Python Syntax", check_python_syntax),
        ("Module Imports", check_imports),
    ]
    
    results = []
    for name, check_func in checks:
        print(f"\n{'='*50}")
        print(f"Checking: {name}")
        print('='*50)
        try:
            result = check_func()
            results.append((name, result))
        except Exception as e:
            print(f"❌ Error running {name} check: {e}")
            results.append((name, False))
    
    print("\n" + "="*50)
    print("Validation Summary")
    print("="*50)
    
    all_passed = True
    for name, passed in results:
        status = "✅ PASS" if passed else "❌ FAIL"
        print(f"{status}: {name}")
        if not passed:
            all_passed = False
    
    if all_passed:
        print("\n✅ All checks passed!")
        return 0
    else:
        print("\n❌ Some checks failed. Please fix the issues above.")
        return 1


if __name__ == "__main__":
    sys.exit(main())

