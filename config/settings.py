# Yousef (Ibrahim) Gomaa - ID: 320210207
# Egypt-Japan University of Science and Technology
# Artificial Intelligence and Data Science Department
# Tic-Tac-Toe Version Info
# ---
''' This dictionary contains all of the data
     needed to be used globally.
     In the event of failure, kindly refer to
     the version info stated in the deployed app.'''
settings = {"version": "0.0.2",
            "day": 14,
            "month": 10,
            "year": 2023}

class VersionInfo():
    ''' Class that contains all related info regarding the deployment.'''
    def get_date():
        ''' Generate date of the current application version in DD/MM/YYYY format.'''
        return "{d}/{m}/{y}".format(d = settings['day'], m = settings['month'], y = settings['year'])

    def get_title():
        ''' Generate project title'''
        return "Day&Night V.{v} - tic-tac-toe - {d}".format(v = settings['version'], d = VersionInfo.get_date())