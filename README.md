### How do I run the project locally?

You will need to install the new requirements. `pip install -r requirements.txt`

You can then type: `flask run` to start the application.


### I need to create an environment variable, how do I do that?

In the root directory create a `.env` file and put your variables in there. For
example `SECRET_KEY='supersecret'`. These will be loaded by dotenv, you can
then access them how you normally would via `os.getenv`.

### I am only working on the frontend, where do I put my files?

#### HTML Files

These should all be included in the `src/templates/` directory.

#### CSS and JS

You will need to store these in the `src/static/css` and `src/static/js`
directories respectively.

#### How do I link my css and js to my HTML?

In your html file you will need to use the following format (you can copy and paste the following and change FILENAME to your filename):

```
CSS:
<link ref="stylesheet" href=" {{ url_for('static', filename='css/<FILENAME>') }} ">

JS:

<script src=" url_for('static', filename='js/<FILENAME>') "></script>

```

For example, I have created a style sheet in `src/static/css` called `style.css`. I want to use this in my `src/templates/index.html` file so I would write the following in the head section of my html file:

` <link ref="stylesheet" href=" {{ url_for('static', filename='css/style.css') }} "> `

If this doens't make sense, just ask in slack!




