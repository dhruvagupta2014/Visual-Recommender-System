# Mnist  webapp demo (Flask)

**[Heroku live web-app][heroku-app-url]**

**[Detail blog](https://sumit-kothari.github.io/flask-deployment/)** explaining the code.

**Table of Contents**
- [Pre-request][pre-request]
- [Usage / Installation][usage]
- [Code structure][code_structure]


# <a name="pre-request"></a>Pre-request

You should have basic understanding of:
- Python3, pip, virtual environment, Flask
- Machine Learning / Deep Learning
- HTML, CSS, JavaScript



# <a name="usage"></a>Usage / Installation

### Local

Clone/download code for this demo from [mnist-demo github repo][repo_url]

```bash
git clone https://github.com/sumit-kothari/mnist-demo.git
```

Navigate to root of the project and install required dependencies

```bash
cd mnist-demo
pip install -r requirements.txt
```

Run Flask app locally
```bash
python app.py
```

### Deploy to heroku

[![Deploy](https://www.herokucdn.com/deploy/button.png)](https://heroku.com/deploy?template=https://github.com/sumit-kothari/mnist-demo/tree/master)



# <a name="code_structure"></a>Code Structure

![_code_structure.png](https://sumit-kothari.github.io/images/code_structure.png)



[pre-request]: #pre-request
[usage]: #usage
[code_structure]: #code_structure
[ml-model]: #ml-model
[web-app]: #web-app
[integration]: #integration
[deployment]: #deployment
[train-mnist.py]: https://github.com/sumit-kothari/mnist-demo/blob/master/tensorflow_model/train-mnist.py
[predict.py]: https://github.com/sumit-kothari/mnist-demo/blob/master/tensorflow_model/predict.py
[index.html]: https://github.com/sumit-kothari/mnist-demo/blob/master/templates/index.html
[predict.html]: https://github.com/sumit-kothari/mnist-demo/blob/master/templates/predict.html
[heroku-app-url]: https://mnist-demo-app.herokuapp.com/
[repo_url]: https://github.com/sumit-kothari/mnist-demo
