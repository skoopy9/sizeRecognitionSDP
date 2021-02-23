from kb.generator.kariertes_blatt import get_oben_data_objects_generator, get_seite_data_objects_generator, \
    get_unter_data_objects_generator
from kb.training.classification_training import train_model

root_path = './data/data_objects'
data_generator = [
    get_oben_data_objects_generator,
    get_seite_data_objects_generator,
    get_unter_data_objects_generator
]

data_generator_name = [
    "models/classification_oben.hdf5",
    "models/classification_seite.hdf5",
    "models/classification_unter.hdf5",
]

for get_generator, file_output in zip(data_generator, data_generator_name):
    print("Training {name}...".format(name=file_output))
    validation_generator, train_generator, classes = get_generator(root_path)
    print("Train size: {size}".format(size=len(train_generator.x)))
    print("Validation size: {size}".format(size=len(validation_generator.x)))
    train_model(train_generator, validation_generator, classes, file_output=file_output, epochs=16)
