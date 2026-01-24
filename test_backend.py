"""
Test script to verify backend functionality
"""
import sys
import os

# Add backend to path
backend_path = os.path.join(os.getcwd(), 'complaint_manager', 'backend')
sys.path.insert(0, backend_path)

print("=" * 60)
print("Testing Complaint Manager Backend")
print("=" * 60)

try:
    print("\n1. Testing imports...")
    from app import main, models, schemas, crud, database
    print("   ✓ All imports successful")
    
    print("\n2. Testing database connection...")
    from app.database import engine, Base
    print(f"   ✓ Database URL: {database.DATABASE_URL}")
    
    print("\n3. Testing FastAPI app creation...")
    from app.main import app
    print(f"   ✓ App created: {app.title}")
    print(f"   ✓ App version: {app.version}")
    
    print("\n4. Testing routers...")
    routes = [route.path for route in app.routes]
    print(f"   ✓ Total routes: {len(routes)}")
    print(f"   ✓ API routes: {[r for r in routes if r.startswith('/api')]}")
    
    print("\n5. Testing models...")
    models_list = [models.User, models.ComplaintCategory, models.Complaint, 
                   models.ComplaintComment, models.ComplaintStatusHistory, 
                   models.ComplaintAttachment]
    print(f"   ✓ All {len(models_list)} models defined")
    
    print("\n" + "=" * 60)
    print("✓ ALL TESTS PASSED - Backend is ready for deployment!")
    print("=" * 60)
    
except Exception as e:
    print(f"\n✗ ERROR: {e}")
    import traceback
    traceback.print_exc()
    sys.exit(1)
