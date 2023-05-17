import numpy as np 
import pandas as pd 
import os

class openstereo_addon:
    def __init__(self,directory):
        self.directory = directory
         
    def clino_to_txt(self,file,locality=None,unit=None,data_type=None,output_name=None):
        """
        This function allows users to easily **convert .csv files from FieldMove CLINO to a .txt file used by OpenStereo**.
        Input and output files are located in the directory entered in openstereo_addon class parameters. **clino_to_txt** can handle both **plane or line data** without specific user information. 

        Parameters
        ----------
        file : [*'file name'*, ...]
            The parameter 'file' **must be as a list of file name(s) in string format**. The extension '.csv' is not required.
        locality : *'locality'*, optional
            The parameter 'locality' **must match with the locality format in .csv file**. The default is None.
        unit : *'unit'*, optional
            The parameter 'unit' **must match with the unit format in .csv file**. The default is None.
        data_type : *'data type'*, optional
            The parameter 'data_type' **must match with the data type format in .csv file**. The default is None.
        output_name : *'output name'*, optional
            The parameter 'output_name' **must be the name of the output file in string format**. If the default is None, the file name is generated based on previous parameters as **'locality_unit_datatype.txt'**.
        """
        data,file_name = np.empty((0,2)),list()
        for subfile in file:
            if os.path.isfile(os.path.join(self.directory,subfile+'.csv')):
                df = pd.read_csv(os.path.join(self.directory,subfile+'.csv'),header=0)
                df,columns = df.applymap(lambda x: x.replace(' ','') if isinstance(x,str) else x),dict()
                for header in list(df.columns):
                    columns[header] = header.replace(' ','')
                df.rename(columns=columns,inplace=True)
                if locality is not None :
                    locality = locality.replace(' ','')
                    file_name.append(locality)
                    df = df.query(f'localityName == "{locality}"')
                    pass
                if unit is not None :
                    unit = unit.replace(' ','')
                    file_name.append(unit)
                    df = df.query(f'unitId == "{unit}"')
                    pass
                if list(df.columns) == ['localityId','localityName','dataId','x','y','latitude','longitude','zone','altitude','horiz_precision','vert_precision','planeType','dip','dipAzimuth','strike','declination','unitId','timedate','notes']:
                    if data_type is not None :
                        data_type = data_type.replace(' ','')
                        file_name.append(data_type)
                        df = df.query(f'planeType == "{data_type}"')
                        pass
                    data = np.vstack((data,[(round(x['dipAzimuth']),round(x['dip'])) for _,x in df.iterrows()]))
                elif list(df.columns) == ['localityId','localityName','dataId','x','y','latitude','longitude','zone','altitude','horiz_precision','vert_precision','lineationType','plunge','plungeAzimuth','declination','unitId','timedate','notes']:
                    if data_type is not None :
                        data_type = data_type.replace(' ','')
                        file_name.append(data_type)
                        df = df.query(f'lineationType == "{data_type}"')
                        pass
                    data = np.vstack((data,[(round(x['plungeAzimuth']),round(x['plunge'])) for _,x in df.iterrows()]))
        if output_name is not None :
            file_name = output_name.replace(' ','')+'.txt'
            pass
        elif len(file_name) != 0:    
            file_name = '_'.join(file_name)+'.txt'   
        if len(data) != 0 :
            with open(os.path.join(self.directory,file_name),'w') as file:
                for row in data:
                    file.write('\t'.join([str(int(value)) for value in row])+'\n')
