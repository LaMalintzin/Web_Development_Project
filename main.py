from website import create_app

app = create_app()

# Make sure that the right main.py file is running 
if __name__ == '__main__':
    app.run(debug=True)





