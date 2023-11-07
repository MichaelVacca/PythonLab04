from flask import Flask, render_template

app = Flask(__name__)

@app.route('/index', methods=['GET'])
def Index():
    return render_template('index.html')



@app.route('/Sales', methods=['GET'])
def chart_page():  # put application's code here
    # Define Plot Data
    labels = [
        'January',
        'February',
        'March',
        'April',
        'May',
        'June',
    ]
    header = "This is my first line graph"
    description = "THis is a desc"
    data = [0, 10, 15, 8, 22, 18, 25]
    return render_template('line_graph_example.html',data=data , labels=labels , header=header, description=description)


if __name__ == '__main__':
    app.run()
