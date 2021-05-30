from website import create_app

app = create_app()

#entry point for the app
if __name__ == '__main__':
    # debug=True: any change to code, app will automatically rerun
    app.run(debug=True)