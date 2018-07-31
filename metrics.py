import tensorflow as tf
from tensorflow.contrib.keras.api.keras.losses import mean_absolute_error, mean_absolute_percentage_error, mean_squared_error

def calculate_metrics(pred, ys):
    """
    Calculate the MAE, MAPE, RMSE
    :param df_pred:
    :param df_test:
    :param null_val:
    :return:
    """
    mae = mean_absolute_error(ys, pred)
    rmse = tf.sqrt(mean_squared_error(ys, pred))
    mape = mean_absolute_percentage_error(ys,pred)
    return mae, mape, rmse


