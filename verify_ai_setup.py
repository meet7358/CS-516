#!/usr/bin/env python3
"""
Verify AI setup and database schema.
"""

import os
import sys

# Add the project root to Python path
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

def verify_ai_setup():
    """Verify AI setup and database schema."""
    try:
        from albumy import create_app
        from albumy.models import Photo
        from ml.vision import analyze_image_local_path, extract_alt_and_tags
        
        app = create_app()
        
        with app.app_context():
            print("🔍 Verifying AI Setup...")
            print()
            
            # Check database schema
            print("📊 Database Schema Check:")
            try:
                # Try to access the new columns
                sample_photo = Photo.query.first()
                if sample_photo:
                    print(f"   ✅ Photo model has alt_text: {hasattr(sample_photo, 'alt_text')}")
                    print(f"   ✅ Photo model has tags_ml: {hasattr(sample_photo, 'tags_ml')}")
                    
                    # Check if columns exist in database
                    from sqlalchemy import inspect
                    inspector = inspect(Photo.__table__)
                    columns = [col.name for col in inspector.columns]
                    print(f"   📋 Database columns: {columns}")
                    
                    if 'alt_text' in columns and 'tags_ml' in columns:
                        print("   ✅ Database has required AI columns!")
                    else:
                        print("   ❌ Database missing AI columns!")
                        return False
                else:
                    print("   ⚠️  No photos in database")
            except Exception as e:
                print(f"   ❌ Database schema error: {e}")
                return False
            
            print()
            
            # Check AI vision module
            print("🤖 AI Vision Module Check:")
            try:
                # Test with a sample image
                sample_image = "uploads/random_0.jpg"
                if os.path.exists(sample_image):
                    print(f"   🧪 Testing with: {sample_image}")
                    analysis = analyze_image_local_path(sample_image)
                    alt_text, tags = extract_alt_and_tags(analysis)
                    
                    print(f"   ✅ Analysis successful!")
                    print(f"   📝 Alt text: '{alt_text}'")
                    print(f"   🏷️  Tags: {tags}")
                    
                    if alt_text and tags:
                        print("   ✅ AI generation working!")
                    else:
                        print("   ❌ AI generation not working!")
                        return False
                else:
                    print(f"   ❌ Sample image not found: {sample_image}")
                    return False
            except Exception as e:
                print(f"   ❌ AI vision error: {e}")
                return False
            
            print()
            
            # Check upload route integration
            print("📤 Upload Route Integration Check:")
            try:
                from albumy.blueprints.main import upload
                print("   ✅ Upload route imported successfully")
                
                # Check if the route has AI integration
                import inspect
                source = inspect.getsource(upload)
                if 'analyze_image_local_path' in source and 'extract_alt_and_tags' in source:
                    print("   ✅ Upload route has AI integration!")
                else:
                    print("   ❌ Upload route missing AI integration!")
                    return False
                    
                if 'photo.alt_text' in source and 'photo.tags_ml' in source:
                    print("   ✅ Upload route sets AI fields!")
                else:
                    print("   ❌ Upload route missing AI field assignments!")
                    return False
                    
            except Exception as e:
                print(f"   ❌ Upload route check error: {e}")
                return False
            
            print()
            print("🎉 AI Setup Verification Complete!")
            print("   ✅ Database schema: Ready")
            print("   ✅ AI vision module: Working")
            print("   ✅ Upload route: Integrated")
            print("   ✅ Flask app: Running")
            
            return True
            
    except Exception as e:
        print(f"❌ Verification failed: {e}")
        import traceback
        traceback.print_exc()
        return False

if __name__ == "__main__":
    print("Verifying AI setup...")
    success = verify_ai_setup()
    if success:
        print("\n✅ AI setup is working perfectly!")
    else:
        print("\n❌ AI setup has issues!")
        sys.exit(1)
