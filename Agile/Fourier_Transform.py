import numpy as np
import cv2
import matplotlib.pyplot as plt

image = cv2.imread('/home/cusat/Pictures/my_image.png', cv2.IMREAD_GRAYSCALE)

image = np.float32(image)

f = np.fft.fft2(image)  
fshift = np.fft.fftshift(f)  

magnitude_spectrum = np.log(np.abs(fshift) + 1)

energy_spatial = np.sum(image**2)

energy_frequency = np.sum(np.abs(fshift)**2)

energy_preservation = np.isclose(energy_spatial, energy_frequency)

print(f"Energy in Spatial Domain: {energy_spatial}")
print(f"Energy in Frequency Domain: {energy_frequency}")
print(f"Energy Preservation (spatial = frequency): {energy_preservation}")

plt.figure(figsize=(15, 10))

plt.subplot(2, 3, 1)
plt.imshow(image, cmap='gray')
plt.title('Original Image (Spatial Domain)')
plt.axis('off')

plt.subplot(2, 3, 2)
plt.imshow(magnitude_spectrum, cmap='gray')
plt.title('Magnitude Spectrum (Frequency Domain)')
plt.axis('off')

phase_spectrum = np.angle(fshift)
plt.subplot(2, 3, 3)
plt.imshow(phase_spectrum, cmap='hsv')
plt.title('Phase Spectrum (Frequency Domain)')
plt.axis('off')

f_ishift = np.fft.ifftshift(fshift)
image_reconstructed = np.fft.ifft2(f_ishift)
image_reconstructed = np.abs(image_reconstructed)

plt.subplot(2, 3, 4)
plt.imshow(image_reconstructed, cmap='gray')
plt.title('Reconstructed Image (Inverse Fourier)')
plt.axis('off')

plt.subplot(2, 3, 5)
plt.plot([0, 1], [energy_spatial, energy_frequency], marker='o', markersize=5, label="Energy Comparison")
plt.ylabel("Energy")
plt.title('Energy Preservation Check')
plt.xticks([0, 1], ['Spatial Domain', 'Frequency Domain'])
plt.legend()

plt.tight_layout()
plt.savefig('output.png')  # Save as output.png
plt.close()  
