from tkinter import messagebox

import numpy as np
from pydicom.dataset import Dataset, FileDataset
from pydicom.uid import ExplicitVRLittleEndian
import pydicom._storage_sopclass_uids
from skimage.exposure import rescale_intensity
from skimage.util import img_as_ubyte


#from skimage.util import img_as_ubyte
#from skimage.exposure import rescale_intensity

def convert_img(img):
    return img_as_ubyte(rescale_intensity(img, out_range=(0.0, 1.0)))


def dicom_read(file_name):
    # load dicom file
    ds = pydicom.dcmread(file_name)

    print("DICOM info")
    print("Patient Name:", ds.PatientName)
    print("Patient ID:", ds.PatientID)
    #print("Study date:", ds.StudyDate)
    print("Image comments:", ds.ImageComments)
    print("Modality:", ds.Modality)
    print("Image size:", ds.Rows, "x", ds.Columns)

def dicom_save(file_name, img, patient_data):
    img_converted = convert_img(img)

    meta = Dataset()
    meta.MediaStorageSOPClassUID = pydicom._storage_sopclass_uids.CTImageStorage
    meta.MediaStorageSOPInstanceUID = pydicom.uid.generate_uid()
    meta.TransferSyntaxUID = pydicom.uid.ExplicitVRLittleEndian

    ds = FileDataset(None, {}, preamble=b"\0" * 128)
    ds.file_meta = meta

    ds.is_little_endian = True
    ds.is_implicit_VR = False

    ds.SOPClassUID = pydicom._storage_sopclass_uids.CTImageStorage
    ds.SOPInstanceUID = meta.MediaStorageSOPInstanceUID

    ds.PatientName = patient_data["PatientName"]
    ds.PatientID = patient_data["PatientID"]
    ds.ImageComments = patient_data["ImageComments"]

    ds.Modality = "CT"
    ds.SeriesInstanceUID = pydicom.uid.generate_uid()
    ds.StudyInstanceUID = pydicom.uid.generate_uid()
    ds.FrameOfReferenceUID = pydicom.uid.generate_uid()

    ds.BitsStored = 8
    ds.BitsAllocated = 8
    ds.SamplesPerPixel = 1
    ds.HighBit = 15

    ds.ImagesInAcquisition = 1
    ds.InstanceNumber = 1

    ds.Rows, ds.Columns = img_converted.shape[:2]

    ds.ImageType = r"ORIGINAL\PRIMARY\AXIAL"

    ds.PhotometricInterpretation = "MONOCHROME2"
    ds.PixelRepresentation = 0

    pydicom.dataset.validate_file_meta(ds.file_meta, enforce_standard=True)

    ds.PixelData = img_converted.tobytes()

    ds.save_as(file_name, write_like_original=False)

