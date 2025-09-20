#!/usr/bin/env python3
"""
Check recent photos for AI descriptions and display them.
"""

import os
import sys

# Add the project root to Python path
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

def check_recent_ai_photos():
    """Check recent photos for AI descriptions."""
    try:
        from albumy import create_app
        from albumy.models import Photo
        
        app = create_app()
        
        with app.app_context():
            print("🔍 Checking Recent Photos for AI Descriptions...")
            print()
            
            # Get the 5 most recent photos
            recent_photos = Photo.query.order_by(Photo.timestamp.desc()).limit(5).all()
            
            if not recent_photos:
                print("❌ No photos found in database!")
                return False
            
            print(f"📸 Found {len(recent_photos)} recent photos:")
            print()
            
            for i, photo in enumerate(recent_photos, 1):
                print(f"📷 Photo #{i} (ID: {photo.id})")
                print(f"   📁 Filename: {photo.filename}")
                print(f"   👤 Author: {photo.author.name}")
                print(f"   📅 Uploaded: {photo.timestamp}")
                print(f"   📝 User Description: {photo.description or 'None'}")
                print(f"   🤖 AI Alt Text: {photo.alt_text or 'None'}")
                print(f"   🏷️  AI Tags: {photo.tags_ml or 'None'}")
                
                if photo.alt_text or photo.tags_ml:
                    print("   ✅ Has AI-generated content!")
                else:
                    print("   ❌ No AI-generated content")
                
                print()
            
            # Count photos with AI content
            ai_photos = Photo.query.filter(
                (Photo.alt_text.isnot(None)) | (Photo.tags_ml.isnot(None))
            ).count()
            
            total_photos = Photo.query.count()
            
            print(f"📊 AI Content Summary:")
            print(f"   Total photos: {total_photos}")
            print(f"   Photos with AI content: {ai_photos}")
            print(f"   AI coverage: {(ai_photos/total_photos*100):.1f}%" if total_photos > 0 else "   AI coverage: 0%")
            
            if ai_photos > 0:
                print("\n🎉 AI descriptions are working!")
                print("   - Upload new photos to see AI descriptions")
                print("   - Check individual photo pages for AI content")
                print("   - Use search to find photos by AI tags")
            else:
                print("\n⚠️  No AI content found in recent photos")
                print("   - Try uploading a new photo")
                print("   - Check if the upload route is working")
            
            return True
            
    except Exception as e:
        print(f"❌ Error checking photos: {e}")
        import traceback
        traceback.print_exc()
        return False

if __name__ == "__main__":
    print("Checking recent photos for AI descriptions...")
    success = check_recent_ai_photos()
    if success:
        print("\n✅ Photo check complete!")
    else:
        print("\n❌ Photo check failed!")
        sys.exit(1)
