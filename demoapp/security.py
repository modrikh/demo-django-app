"""Middleware minimaliste de securite (CSP, Permissions-Policy, cache)."""


class SecurityHeadersMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        response = self.get_response(request)
        response["Content-Security-Policy"] = (
            "default-src 'self'; style-src 'self' 'unsafe-inline'; "
            "script-src 'self'; img-src 'self' data:; frame-ancestors 'none'"
        )
        response["Permissions-Policy"] = "geolocation=(), microphone=(), camera=()"
        response["X-Content-Type-Options"] = "nosniff"
        response["Referrer-Policy"] = "no-referrer"
        return response