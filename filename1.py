def funciya():
    x1 = 0.2
    x2 = 5
    x3 = 5
    x4 = 20
    x5 = 0.5
    if x4 <= 20.07:
        if x3 <= 5.97:
            if x1 <= 0.29:
                if x5 <= 0.53:
                    clas = 2
                if x5 >  0.53:
                    clas = 1
            if x1 >  0.29:
                if x2 <= -0.27:
                    if x1 <= 0.37:
                        if x4 <= 17.05:
                            clas = 1
                        if x4 >  17.05:
                            clas = 2
                    if x1 >  0.37:
                        if x2 <= -0.27:
                            clas = 1
                        if x2 >  -0.27:
                            clas = 1
                if x2 >  -0.27:
                    clas = 1
        if x3 >  5.97:
            if x3 <= 6.14:
                clas = 2
            if x3 >  6.14:
                if x1 <= 0.26:
                    clas = 2
                if x1 >  0.26:
                    clas = 1
    if x4 >  20.07:
        if x1 <= 0.42:
            if x3 <= 5.40:
                clas = 1
            if x3 >  5.40:
                if x1 <= 0.33:
                    clas = 2
                if x1 >  0.33:
                    if x1 <= 0.35:
                        if x4 <= 28.02:
                            clas = 1
                        if x4 >  28.02:
                            clas = 2
                    if x1 >  0.35:
                        clas = 2
        if x1 >  0.42:
            clas = 1
    return clas