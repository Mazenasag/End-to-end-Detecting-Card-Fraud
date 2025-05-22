import joblib
import numpy as np
from pathlib import Path


class PredictionPipeline:
    def __init__(self, model_path, scaler_path):
        self.model = joblib.load(model_path)
        self.scaler = joblib.load(scaler_path)

    def predict(self, input_data: list):
        # Ensure input is in shape (1, n_features)
        input_array = np.array(input_data).reshape(1, -1)
        scaled_input = self.scaler.transform(input_array)
        prediction = self.model.predict(scaled_input)
        return prediction[0]


# if __name__ == "__main__":

#     obj = PredictionPipeline(Path("artifacts/model.pkl"),
#                              Path("artifacts\scaler.pkl"))
#     input_fet = [-16.5265065691231, 8.58497179585822, -18.6498531851945, 9.50559351508723, -13.7938185270957, -2.83240429939747, -16.701694296045, 7.51734390370987, -8.50705863675898, -14.1101844415457, 5.29923634963938, -10.8340064814734, 1.67112025332681, -9.37385858364976,
#                  0.360805641631617, -9.89924654080666, -19.2362923697613, -8.39855199494575, 3.10173536885404, -1.51492343527852, 1.19073869481428, -1.12767000902061, -2.3585787697881, 0.673461328987237, -1.4136996745882, -0.46276236139933, -2.01857524875161, -1.04280416970881, 364.19]
#     result = obj.predict(input_fet)
#     print("Prediction:", result)
