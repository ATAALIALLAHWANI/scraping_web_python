import ScrapingWuzzuf
import matplotlib.pyplot as plt
def mian():
    data = ScrapingWuzzuf.extraction()
    PythonDeveloper = []
    PythonAI = []

    PythonBackend = []
    DataScience = []




    for g in range(len(data)):
        data[g] = data[g].upper()


    for i in range(len(data)):

        if "PYTHON DEVELOPER" in data[i]:
            PythonDeveloper.append(data[i])

        if "Artificial Intelligence" in data[i] or "AI " in data[i]:
            PythonAI.append(data[i])

        if "PYTHON BACKEND" in data[i] or "PYTHON FULL STACK" in data[i]:
            PythonBackend.append(data[i])

        if "DATA SCIENCE" in  data[i]:
            DataScience.append(data[i])

    print(data)
    print(PythonAI)
    # visualiztion


    list_program_field = ["PYTHON DEVELOPER" , "Artificial Intelligence" , "PYTHON BACKEND" ,"DATA SCIENCE" ]
    num_people_infield = [len(PythonDeveloper) , len(PythonAI) , len(PythonBackend) ,len(DataScience)]
    figure_size = (10, 10)
    figure_dpi = 90
    n_rows = 2
    n_columns = 1

    fig = plt.figure(figsize=figure_size, dpi=figure_dpi)

    ax1 = fig.add_subplot(n_rows, n_columns, 1)
    ax1.bar(x=list_program_field, height=num_people_infield, color='orange', label="number people")
    ax1.set_xlabel(" Programming field ")
    ax1.set_ylabel(" companies hiring in jordan ")
    ax1.set_title("  info ")

    ax1.grid(True)
    ax1.legend()

    plt.show()


 #  othar work
# list_program_field = list(first_felid.keys())
# num_people_infield = list(first_felid.values())
 # feild_count = {}
    #
    #
    # for i in range(len(data)):
    #     if data[i] in feild_count:
    #         feild_count[data[i]] +=1
    #     else:
    #         feild_count[data[i]] = 1
    #
    # first_felid = dict(list(feild_count.items())[:2])
