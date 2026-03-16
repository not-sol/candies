def app_controller(app):
    from controllers.file_controller import router as file_router
    from controllers.hello_controller import router as hello_router
    from controllers.auth_controller import router as auth_router

    app.include_router(hello_router, prefix="/hello", tags=["hello"])
    app.include_router(file_router, prefix="/file", tags=["file"])
    app.include_router(auth_router, prefix="/auth", tags=["auth"])
