"""Middleware minimaliste de securite (CSP, Permissions-Policy, cache)."""


class SecurityHeadersMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        response = self.get_response(request)
        response["Content-Security-Policy"] = (
            "default-src 'self'; style-src 'self'; "
            "script-src 'self'; img-src 'self' data:; "
            "frame-ancestors 'none'; object-src 'none'; base-uri 'none'; "
            "form-action 'self'"
        )
        response["Permissions-Policy"] = "geolocation=(), microphone=(), camera=()"
        response["X-Content-Type-Options"] = "nosniff"
        response["Referrer-Policy"] = "no-referrer"
        response["Cross-Origin-Opener-Policy"] = "same-origin"
        response["Cross-Origin-Embedder-Policy"] = "require-corp"
        response["Cross-Origin-Resource-Policy"] = "same-origin"
        return response