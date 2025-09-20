#!/usr/bin/env python3
"""
Check which photos were uploaded by the current user and have AI descriptions.
"""

import os
import sys

# Add the project root to Python path
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

def check_user_uploads():
    """Check user's uploaded photos with AI descriptions."""
    try:
        from albumy import create_app
        from albumy.models import Photo, User
        
        app = create_app()
        
        with app.app_context():
            print("🔍 Checking Your Uploaded Photos with AI Descriptions...")
            print()
            
            # Get the current user (assuming Grey Li is the main user)
            user = User.query.filter_by(username='greyli').first()
            if not user:
                print("❌ User 'greyli' not found!")
                return False
            
            print(f"👤 Checking photos for user: {user.name} ({user.username})")
            print()
            
            # Get all photos uploaded by this user
            user_photos = Photo.query.filter_by(author_id=user.id).order_by(Photo.timestamp.desc()).all()
            
            if not user_photos:
                print("❌ No photos found for this user!")
                return False
            
            print(f"📸 Found {len(user_photos)} photos uploaded by {user.name}:")
            print()
            
            ai_photos = []
            no_ai_photos = []
            
            for i, photo in enumerate(user_photos, 1):
                print(f"📷 Photo #{i} (ID: {photo.id})")
                print(f"   📁 Filename: {photo.filename}")
                print(f"   📅 Uploaded: {photo.timestamp}")
                print(f"   📝 User Description: {photo.description or 'None'}")
                print(f"   🤖 AI Alt Text: {photo.alt_text or 'None'}")
                print(f"   🏷️  AI Tags: {photo.tags_ml or 'None'}")
                
                if photo.alt_text or photo.tags_ml:
                    print("   ✅ Has AI-generated content!")
                    ai_photos.append(photo)
                else:
                    print("   ❌ No AI-generated content")
                    no_ai_photos.append(photo)
                
                print()
            
            # Summary
            print("📊 Summary:")
            print(f"   Total photos by {user.name}: {len(user_photos)}")
            print(f"   Photos with AI content: {len(ai_photos)}")
            print(f"   Photos without AI content: {len(no_ai_photos)}")
            print(f"   AI coverage: {(len(ai_photos)/len(user_photos)*100):.1f}%")
            
            if ai_photos:
                print()
                print("✅ Photos with AI Descriptions:")
                for photo in ai_photos:
                    print(f"   - {photo.filename}: '{photo.alt_text}'")
            
            if no_ai_photos:
                print()
                print("❌ Photos without AI Descriptions:")
                for photo in no_ai_photos:
                    print(f"   - {photo.filename}: No AI content")
            
            print()
            print("🎯 Recommendation:")
            if len(ai_photos) > 0:
                print("   ✅ Your recent uploads have AI descriptions!")
                print("   ✅ AI system is working for your photos!")
            else:
                print("   ⚠️  No AI descriptions found for your photos")
                print("   💡 Try uploading a new photo to test AI features")
            
            return True
            
    except Exception as e:
        print(f"❌ Error checking user uploads: {e}")
        import traceback
        traceback.print_exc()
        return False

if __name__ == "__main__":
    print("Checking your uploaded photos...")
    success = check_user_uploads()
    if success:
        print("\n✅ User upload check complete!")
    else:
        print("\n❌ User upload check failed!")
        sys.exit(1)
