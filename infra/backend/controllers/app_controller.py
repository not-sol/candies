def app_controller(app):
    from controllers.file_controller import router as file_router
    from controllers.hello_controller import router as hello_router

    app.include_router(hello_router, prefix="/hello", tags=["hello"])
    app.include_router(file_router, prefix="/files", tags=["files"])
