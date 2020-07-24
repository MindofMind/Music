#Define the callback to save the best model during training:

mc=ModelCheckpoint('best_model.h5', monitor='val_loss', mode='min', save_best_only=True,verbose=1)

#Let’s train the model with a batch size of 128 for 50 epochs:

history = model.fit(np.array(x_tr),np.array(y_tr),batch_size=128,epochs=50, validation_data=(np.array(x_val),np.array(y_val)),verbose=1, callbacks=[mc])

#Loading the best model:

#loading best model
from keras.models import load_model
model = load_model('best_model.h5')
