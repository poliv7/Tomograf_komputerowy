import math
from algorithm_Bresenham import *
from dicom import *

def tomograf(in_image, step, d, beta, iterations):
    # promien, (-1 ze wzgledu na to, zeby okrag nie wyszedl poza obrazek
    r = min(in_image.shape[0], in_image.shape[1]) / 2 - 1

    # wspolrzedne srodka okregu
    x_przes = in_image.shape[0] / 2
    y_przes = in_image.shape[1] / 2

    # macierze, ustawienie poczatkowych wartosci
    sinogram = np.zeros(shape=(math.ceil(360 / step), d))  # wyswietli sinogram
    out_image = np.zeros(shape=(in_image.shape[0], in_image.shape[1]))  # wyswietli obraz wyjsciowy
    # nieodwiedzony bedzie czarny, uzyskamy srednia wartosc jasnosci pixeli w obrazie wyjsciowym, uzyte w ten sposob dopiero w linii 58
    visited = np.zeros(shape=(in_image.shape[0], in_image.shape[1]))

    # przejscie o kat od 0 do 360 o wartosc step, wypelnia wiersze, kat miedzy emiterami
    for angle in range(0, iterations * step, step):
        # wspolrzedne emitera
        emiter_x = round(math.cos(math.radians(angle)) * r + x_przes)
        emiter_y = round(math.sin(math.radians(angle)) * r + y_przes)

        # wypelnia kolumny 0 do ilosci wiazek
        for i in range(0, d):
            alfa = calculate_distance_between_detectors(angle, beta, d, i)  # kat miedzy detektorami
            # wspolrzedne detektora, aby detektory i emitery poruszaly sie po tym samym okregu
            detector_x = round(math.cos(alfa) * r + x_przes)
            detector_y = round(math.sin(alfa) * r + y_przes)

            # wyliczenie sinogramu, dla kazdego pkt
            sinogram[angle // step][i] = bresenham_for_sinogram(emiter_x, emiter_y, detector_x, detector_y, in_image, visited)
            # wyliczenie obrazu wyjsciowego , na podstawie sinogramu, uzywamy wyznaczonych pixeli
            bresenham_for_output_image(emiter_x, emiter_y, detector_x, detector_y, sinogram[angle // step][i], out_image)

    process_output_image(out_image, visited)

    # normalizacja i konwertowanie ze skali 0-1 na 0-255 dla gui
    sinogram = normalize_and_convert_to_256(sinogram)
    out_image = normalize_and_convert_to_256(out_image)

    patient_data = {"PatientName": "zbigniew wodecki", "PatientID": "100", "ImageComments": "xyzabcde"}
    dicom_save("wynik.dcm", out_image, patient_data)

    return sinogram, out_image


def calculate_distance_between_detectors(emitter_angle, beta, d, detector_index):
    if d == 1:  # dla jednej wiazki, detektor na przeciwko emitera
        return math.radians(emitter_angle) + math.pi
    else:  # przejscie pomiedzy detektorami, jak wiecej niz jeden detektor to zaczynamy od lewej
        return math.radians(emitter_angle) + math.pi - (math.radians(beta) / 2) + (detector_index * (math.radians(beta)) / (d - 1))


def process_output_image(out_image, visited):
    visited[visited == 0] = 1
    out_image /= visited  # normalizacja, odpowiedzialne za jasnosc pixeli w obrazie wyjsciowym

    # z wszystkich komorek tworzymy liste, eliminujemy powtorzenia, sortujemy liste, usuwamy 1 element = 0
    out_image_list = list(set(out_image.flatten()))
    out_image_list.sort()
    out_image_list.remove(0)

    # najmniejszy element przypisujemy tam gdzie jest 0 w obrazie wyjsciowym
    out_image[out_image == 0] = min(out_image_list)

# funkcja normalizacji konwertowania ze skali 0-1 na 0-255 dla gui
def normalize_and_convert_to_256(image):
    return ((image - np.min(image)) / (np.max(image) - np.min(image))) * 255

