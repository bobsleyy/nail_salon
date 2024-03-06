def app_version(request):
    """"Context_processor z nazwą aplikacji oraz jej wersją"""
    return {
        "APP_NAME":  "nail-salon-app",
        "APP_VERSION": "1.0.0"
    }
