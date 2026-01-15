# Mask Detection using CNN (With Mask vs Without Mask)

This project detects whether a person is **wearing a mask** or **not wearing a mask** using deep learning (CNN).

Two implementations are provided based on how the images are loaded and processed:

---

## Dataset Structure

Your dataset must follow this directory structure:
dataset/
├── with_mask/
└── without_mask/


- `with_mask/` → Images of people wearing masks
- `without_mask/` → Images of people without masks

---

# VERSION 1 — Using `cv2` (Manual Loading)

### Method Overview

This version:

- Loads images manually with `cv2`
- Converts BGR → RGB
- Normalizes pixel values
- Splits dataset using `train_test_split`
- Builds a CNN manually in Keras
- Shows training graphs (accuracy & loss)
- Predicts on custom images

### Advantages

- Gives full control over image processing
- Shows how datasets are prepared internally
- Useful for learning how CNNs handle images

### Disadvantages

- No automatic augmentation
- Slower manual loading for large datasets

---

# VERSION 2 — Using `ImageDataGenerator`

### Method Overview

This version:

- Uses `flow_from_directory`
- Performs automatic data augmentation
- Performs automatic validation split
- Optimized for training pipelines

### Included Augmentations:

- Rotation
- Zoom
- Width Shift
- Height Shift
- Shear
- Horizontal Flip

### Advantages

- Faster training setup
- Built-in augmentation improves accuracy
- Works well for small datasets

### Disadvantages

- Less transparent image processing compared to manual cv2 loading

---

# Features Included in Both Versions

✔ CNN with convolution + pooling layers  
✔ Dropout for regularization  
✔ Binary classification (`with_mask` vs `without_mask`)  
✔ ModelCheckpoint (best model saving)  
✔ EarlyStopping (reduce overfitting)  
✔ Training plots (Accuracy & Loss)  
✔ Custom image prediction function  

---

# Comparison Table

| Feature | Version 1 (cv2) | Version 2 (Generator) |
|---|---|---|
| Image Loader | Manual | Automatic |
| Data Augmentation | Manual | Built-in |
| Validation Split | Manual | Built-in |
| Code Complexity | Higher | Lower |
| Best For | Learning processing internals | Faster training |

---

# Outputs

After training you get:

- Trained Model: `mask_detector.h5` / `mask_detector_model_2.h5`
- Test accuracy results
- Training graphs
- Prediction function for new images

---

# How to Use

1. Prepare dataset structure
2. Run notebook (`.ipynb`)
3. Train model (Version 1 or Version 2)
4. Test using prediction function

---

