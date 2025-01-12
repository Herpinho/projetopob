def treino():
    retratos_treino = [cv2.imread("Fotos de Treino/MD01.jpg",cv2.IMREAD_GRAYSCALE),
                    cv2.imread("Fotos de Treino/MD02.jpg",cv2.IMREAD_GRAYSCALE),
                    cv2.imread("Fotos de Treino/MD04.jpg",cv2.IMREAD_GRAYSCALE),
                    cv2.imread("Fotos de Treino/S01.jpg",cv2.IMREAD_GRAYSCALE),
                    cv2.imread("Fotos de Treino/S02.jpg",cv2.IMREAD_GRAYSCALE)]
    labels = [0,0,0,1,1]

    retratos_treino = [np.asarray(img) for img in retratos_treino]
    labels = np.array(labels)
    if recognizer.train(retratos_treino, np.array(labels)):
        return True