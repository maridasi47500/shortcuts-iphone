from flask import Flask, request, jsonify
from shortcuts import Shortcut  # your custom Shortcut class
from flask import Flask, render_template
from flask import Flask, request, redirect, render_template
import os
from shortcuts import Shortcut
import subprocess




import os

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = 'uploads'
os.makedirs(app.config['UPLOAD_FOLDER'], exist_ok=True)


@app.route('/sign-shortcut', methods=['POST'])
def sign_shortcut():
    input_name = request.form.get('shortcut_file')  # from hidden input
    output_name = request.form.get('output_name', 'MySignedSC.shortcut')

    input_path = os.path.join(app.config['UPLOAD_FOLDER'], input_name)
    output_path = os.path.join(app.config['UPLOAD_FOLDER'], output_name)

    subprocess.run([
        'shortcuts', 'sign',
        '--mode', 'people-who-know-me',
        '--input', input_path,
        '--output', output_path
    ])

    return f'''
        Shortcut signed successfully.<br>
        <a href="/download/{output_name}">Download Signed Shortcut</a>
    '''




@app.route('/toml-to-shortcut', methods=['POST'])
def toml_to_shortcut():
    toml_file = request.files.get('toml_path')
    output_name = request.form.get('output_path', 'output.shortcut')
    print(toml_file, output_name)

    if not toml_file:
        return "No TOML file uploaded", 400

    toml_path = os.path.join(app.config['UPLOAD_FOLDER'], toml_file.filename)
    toml_file.save(toml_path)

    output_path = os.path.join(app.config['UPLOAD_FOLDER'], output_name)
    sc = Shortcut()
    #sc.load_toml(toml_path)
    sc.dump(output_path)
    hey="shortcuts examples/"+output_path+" "+output_path.replace(".toml",".shortcut")+""
    subprocess.run(hey.split(" "))


    return f'''
        SHORTCUT file created.<br>
        <a href="/download/{output_name}">Download SHORTCUT file</a>
<form action="/sign-shortcut" method="post" enctype="multipart/form-data">
    <input type="hidden" value="{ output_name }" id="shortcut_file" name="shortcut_file"><br><br>

    <label for="output_name">Signed Output Name:</label><br>
    <input type="text" id="output_name" name="output_name" value="MySigned{ output_name }"><br><br>

    <input type="submit" value="Sign Shortcut">
</form>
    '''

@app.route('/someform')
def pythonform():
    return render_template('form.html')
@app.route('/myform', methods=["POST"])
def heypythonform():
    return render_template('form.html')

@app.route('/')
def welcome():
    return render_template('index.html', maliste=os.listdir("uploads"))



@app.route('/shortcut-to-toml', methods=['POST'])
def shortcut_to_toml():
    shortcut_file = request.files.get('shortcut_path')
    output_name = request.form.get('output_path', 'output.toml')

    if not shortcut_file:
        return "No shortcut file uploaded", 400

    shortcut_path = os.path.join(app.config['UPLOAD_FOLDER'], shortcut_file.filename)
    shortcut_file.save(shortcut_path)

    output_path = os.path.join(app.config['UPLOAD_FOLDER'], output_name)
    sc = Shortcut()
    sc.load_shortcut(shortcut_path)
    sc.dump_toml(output_path)

    return f'''
        TOML file created.<br>
        <a href="/download/{output_name}">Download TOML file</a>
        <h2>Sign a Shortcut File</h2>


    '''

@app.route('/download/<filename>')
def download_file(filename):
    return send_from_directory(app.config['UPLOAD_FOLDER'], filename, as_attachment=True)



@app.route('/python-to-shortcut-or-toml', methods=['POST'])
def python_to_shortcut_or_toml():
    format_type = request.json.get('format')  # 'shortcut' or 'toml'
    output_path = request.json.get('output_path', f'output.{format_type}')
    
    sc = Shortcut()
    sc.actions = [
        actions.AskAction(data={'question': 'What is your name?'}),
        actions.SetVariableAction(data={'name': 'name'}),
        actions.ShowResultAction(data={'text': 'Hello, {{name}}!'})
    ]
    
    if format_type == 'shortcut':
        sc.dump_shortcut(output_path)
    elif format_type == 'toml':
        sc.dump_toml(output_path)
    else:
        return jsonify({'error': 'Invalid format type'}), 400

    return jsonify({'message': f'{format_type} file created', 'path': output_path})

if __name__ == '__main__':
    #app.run(host="192.168.1.18", port="4000", debug=True)
    app.run(port="4000", debug=True)

