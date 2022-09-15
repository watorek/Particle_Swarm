from functools import cached_property

import pandas as pd


class File_Analyzer:
    def __init__(self, file_path):
        self.file_path = file_path
        self.analyzed_file = pd.read_csv(file_path, sep=";")
        self.sample_size = 60
        
        # setting up axis
        self.x_accelerator_axis = self.analyzed_file.iloc[1200:, 1]
        self.y_accelerator_axis = self.analyzed_file.iloc[1200:, 2]
        self.z_accelerator_axis = self.analyzed_file.iloc[1200:, 3]

    #calculations
    #############

    #mean value

    @cached_property
    def mean_value_summary(self):
        mean_value_summary = {
            "Mean value for x axis": self.x_accelerator_axis.mean(),
            "Mean value fo y axis": self.y_accelerator_axis.mean(),
            "Mean value for z axis": self.z_accelerator_axis.mean(),
        }
        return mean_value_summary

    #mean absolute deviation

    @cached_property
    def mean_absolute_deviation_summary(self):
        mean_value_summary = {
            "Mean absolute deviation for x axis": self.x_accelerator_axis.mad(),
            "Mean absolute deviation fo y axis": self.y_accelerator_axis.mad(),
            "Mean absolute deviation for z axis": self.z_accelerator_axis.mad(),
        }
        return mean_value_summary

    #standard deviation

    @cached_property
    def standard_deviation_summmary(self):
        standard_deviation_summary = {
            "Standard deviation for x axis": self.x_accelerator_axis.std(),
            "Standard deviation for y axis": self.y_accelerator_axis.std(),
            "Standard deviation for z axis": self.z_accelerator_axis.std()
        }
        return standard_deviation_summary

    @cached_property
    def median_summary(self):
        median_summary = {
            "Median for x axis": self.x_accelerator_axis.median(),
            "Median for y axis": self.y_accelerator_axis.median(),
            "Median for z axis": self.z_accelerator_axis.median()
        }
        return median_summary

    @cached_property
    def correlation_matrix(self):
        value = self.analyzed_file.corr()
        return value

    @cached_property
    def test_samples(self):
    # TODO : make sure you can try different methods, not just mean value check
        min_mean_value = float(0.7*(self.x_accelerator_axis.mean()))
        max_mean_value = float(1.3*(self.x_accelerator_axis.mean()))

        good_classification = 0
        bad_classification = 0

        for x in range (0, 6000, 60):
            index_max = x + 60
            current_mean = self.x_accelerator_axis[0:60].mean()

            if (current_mean > min_mean_value) and (current_mean < max_mean_value):
                good_classification += 1
            else:
                bad_classification += 1

        result = {
            "Good classifications": good_classification,
            "Bad classifications": bad_classification
        }
        return result


if __name__ == "__main__":

    file1 = "blocked_no_mass.csv"
    file2 = "blocked_60hz_one_mass.csv"
    file3 = "blocked_60hz_two_masses.csv"
    file4 = "blocked_60hz_three_masses.csv"

    blocked_no_mass = File_Analyzer(file1)
    blocked_one_mass = File_Analyzer(file2)
    blocked_two_masses = File_Analyzer(file3)
    blocked_three_masses = File_Analyzer(file4)

    # print(blocked_no_mass.mean_value_summary)
    # print(blocked_one_mass.mean_value_summary)
    # print(blocked_two_masses.mean_value_summary)
    # print(blocked_three_masses.mean_value_summary)

    blocker_no_mass = File_Analyzer(file1)

    print(blocked_no_mass.test_samples)