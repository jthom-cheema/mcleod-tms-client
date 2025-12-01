#!/usr/bin/env python3
"""
Examples of using TMS Client in web frameworks.
These examples show how to serve TMS images through your web backend.
"""

from tms_client import TMSClient, RowTypes

# Initialize your TMS client (usually done once at app startup)
# Option 1: Username/password authentication
tms_client = TMSClient("username", "password")

# Option 2: API key authentication
# tms_client = TMSClient(api_key="your-api-key")

# Option 3: Using environment variables
# Set TMS_USERNAME/TMS_PASSWORD or TMS_API_KEY in .env file
# tms_client = TMSClient()


# === FLASK EXAMPLE ===
def flask_example():
    """Flask endpoint to serve TMS images."""
    from flask import Flask, Response, abort
    
    app = Flask(__name__)
    
    @app.route('/api/images/<load_id>/<image_id>')
    def download_image(load_id, image_id):
        try:
            # Get web-ready image data
            result = tms_client.get_image_for_web(image_id)
            
            # Return as Flask Response
            return Response(
                result['data'],
                mimetype='application/pdf',
                headers=result['headers']
            )
        except Exception as e:
            abort(404, description=f"Image not found: {e}")
    
    @app.route('/api/loads/<load_id>/images')
    def list_images(load_id):
        """List available images for a load."""
        try:
            images = tms_client.get_enriched_images(RowTypes.ORDER, load_id)
            return {
                'load_id': load_id,
                'images': [
                    {
                        'id': img['id'],
                        'name': img['documentTypeName'],
                        'count': img['imageCount'],
                        'download_url': f'/api/images/{load_id}/{img["id"]}'
                    }
                    for img in images
                ]
            }
        except Exception as e:
            abort(404, description=f"Load not found: {e}")


# === FASTAPI EXAMPLE ===
def fastapi_example():
    """FastAPI endpoints to serve TMS images."""
    from fastapi import FastAPI, HTTPException
    from fastapi.responses import Response
    
    app = FastAPI()
    
    @app.get("/api/images/{load_id}/{image_id}")
    async def download_image(load_id: str, image_id: str):
        try:
            # Get web-ready image data
            result = tms_client.get_image_for_web(image_id)
            
            # Return as FastAPI Response
            return Response(
                content=result['data'],
                media_type="application/pdf",
                headers={
                    "Content-Disposition": result['headers']['Content-Disposition'],
                    "Content-Length": result['headers']['Content-Length']
                }
            )
        except Exception as e:
            raise HTTPException(status_code=404, detail=f"Image not found: {e}")
    
    @app.get("/api/loads/{load_id}/images")
    async def list_images(load_id: str):
        """List available images for a load."""
        try:
            images = tms_client.get_enriched_images(RowTypes.ORDER, load_id)
            return {
                'load_id': load_id,
                'images': [
                    {
                        'id': img['id'],
                        'name': img['documentTypeName'],
                        'count': img['imageCount'],
                        'download_url': f'/api/images/{load_id}/{img["id"]}'
                    }
                    for img in images
                ]
            }
        except Exception as e:
            raise HTTPException(status_code=404, detail=f"Load not found: {e}")


# === DJANGO EXAMPLE ===
def django_example():
    """Django views to serve TMS images."""
    from django.http import HttpResponse, Http404, JsonResponse
    from django.views import View
    
    class DownloadImageView(View):
        def get(self, request, load_id, image_id):
            try:
                # Get web-ready image data
                result = tms_client.get_image_for_web(image_id)
                
                # Return as Django HttpResponse
                response = HttpResponse(
                    result['data'],
                    content_type='application/pdf'
                )
                response['Content-Disposition'] = result['headers']['Content-Disposition']
                response['Content-Length'] = result['headers']['Content-Length']
                
                return response
            except Exception as e:
                raise Http404(f"Image not found: {e}")
    
    class ListImagesView(View):
        def get(self, request, load_id):
            try:
                images = tms_client.get_enriched_images(RowTypes.ORDER, load_id)
                return JsonResponse({
                    'load_id': load_id,
                    'images': [
                        {
                            'id': img['id'],
                            'name': img['documentTypeName'],
                            'count': img['imageCount'],
                            'download_url': f'/api/images/{load_id}/{img["id"]}'
                        }
                        for img in images
                    ]
                })
            except Exception as e:
                raise Http404(f"Load not found: {e}")


# === FRONTEND INTEGRATION ===
def frontend_integration_example():
    """
    Frontend JavaScript examples for consuming the API.
    """
    js_example = '''
    // Fetch list of images for a load
    async function getLoadImages(loadId) {
        const response = await fetch(`/api/loads/${loadId}/images`);
        const data = await response.json();
        return data.images;
    }
    
    // Download a specific image
    function downloadImage(loadId, imageId, filename) {
        const url = `/api/images/${loadId}/${imageId}`;
        
        // Create download link
        const link = document.createElement('a');
        link.href = url;
        link.download = filename || 'document.pdf';
        document.body.appendChild(link);
        link.click();
        document.body.removeChild(link);
    }
    
    // Display images in UI
    async function displayLoadImages(loadId) {
        const images = await getLoadImages(loadId);
        
        const container = document.getElementById('images-container');
        container.innerHTML = images.map(img => `
            <div class="image-item">
                <h4>${img.name}</h4>
                <p>${img.count} file(s)</p>
                <button onclick="downloadImage('${loadId}', '${img.id}', '${img.name}.pdf')">
                    Download PDF
                </button>
            </div>
        `).join('');
    }
    '''
    
    return js_example


if __name__ == "__main__":
    print("TMS Client Web Integration Examples")
    print("=" * 40)
    print("This file contains examples for:")
    print("- Flask endpoints")
    print("- FastAPI endpoints") 
    print("- Django views")
    print("- Frontend JavaScript")
    print()
    print("Key benefits of get_image_for_web():")
    print("- Returns binary PDF data")
    print("- Includes proper HTTP headers")
    print("- Handles filename generation")
    print("- Works with all web frameworks")
    print("- Triggers browser download automatically")
