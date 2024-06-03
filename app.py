from flask import Flask, request, render_template
from src.pipeline.prediciton_pipeline import CustomData, PredictPipeline

application = Flask(__name__)
app = application

@app.route('/')
def home_page():
    return render_template('index.html')

@app.route('/predict', methods=['GET', 'POST'])
def predict_datapoint():
    if request.method == 'GET':
        return render_template('form.html')
    else:
        data = CustomData(
            class_label=request.form.get('class'),
            bruises=request.form.get('bruises'),
            gill_spacing=request.form.get('gill-spacing'),
            gill_size=request.form.get('gill-size'),
            gill_color=request.form.get('gill-color'),
            stalk_root=request.form.get('stalk-root'),
            ring_type=request.form.get('ring-type'),
            spore_print_color=request.form.get('spore-print-color')
        )
        final_new_data = data.get_data_as_dataframe()
        predict_pipeline = PredictPipeline()
        pred = predict_pipeline.predict(final_new_data)
        
        # Map prediction result to human-readable format
        if pred[0] == 1:
            result_label = "Edible"
        else:
            result_label = "Poisonous"
            
        return render_template('results.html', final_result=result_label)

if __name__ == "__main__":
    app.run(host='127.0.0.1', debug=True)
