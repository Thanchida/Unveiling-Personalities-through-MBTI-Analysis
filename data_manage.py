import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np


class StoryTelling:

    def __init__(self, controller):
        self.youtube_data = pd.read_csv('Global YouTube Statistics.csv', encoding="latin-1")
        # self.view = view
        self.controller = controller
        self.clean_data()
        self.find_average_earning()

    def clean_data(self):
        # fill missing category with 'Other'
        if self.youtube_data['category'].isnull().any():
            self.youtube_data['category'] = self.youtube_data['category'].fillna('Other')

        # drop row that created_year is missing
        self.youtube_data.dropna(subset=['created_year'], inplace=True)

        # drop row that created_year is 1970 because YouTube is created in 2005
        self.youtube_data = self.youtube_data[self.youtube_data['created_year'] != 1970]

    def find_average_earning(self):
        self.youtube_data['average_monthly_earnings'] = (self.youtube_data['highest_monthly_earnings'] +
                                                         self.youtube_data['lowest_monthly_earnings']) / 2

    def first_story(self, event):
        fig, axs = plt.subplots(1, 3, figsize=(15, 5))
        sns.set_style('darkgrid')
        palette = sns.color_palette("Spectral")

        # First subplot
        ax = sns.regplot(data=self.youtube_data, x='average_monthly_earnings', y='subscribers', ax=axs[0],
                         scatter_kws={'color': palette[5]}, line_kws={'color': palette[1]})
        ax.set_ylim(0)
        ax.set_yticks(ax.get_yticks())
        ax.set_yticklabels([f'{label / 1e6}' for label in ax.get_yticks()])
        ax.set_ylabel('subscribers (million)')

        ax.set_xlim(left=0)
        ax.set_xticks(ax.get_xticks())
        ax.set_xticklabels([f'{label / 1e6}' for label in ax.get_xticks()])
        ax.set_xlabel('average_monthly_earning (million)')

        # Second subplot
        sns.regplot(data=self.youtube_data, x='average_monthly_earnings', y='video views', ax=axs[1],
                    scatter_kws={'color': palette[2]}, line_kws={'color': palette[4]})
        axs[1].set_ylim(0)
        axs[1].set_yticks(axs[1].get_yticks())
        axs[1].set_yticklabels([f'{label / 1e6}' for label in axs[1].get_yticks()])
        axs[1].set_ylabel('video views (million)')

        axs[1].set_xlim(left=0)
        axs[1].set_xticks(axs[1].get_xticks())
        axs[1].set_xticklabels([f'{label / 1e6}' for label in axs[1].get_xticks()])
        axs[1].set_xlabel('average_monthly_earning (million)')

        # Third subplot
        sns.regplot(data=self.youtube_data, x='average_monthly_earnings', y='uploads', ax=axs[2],
                    scatter_kws={'color': palette[2]}, line_kws={'color': 'red'})
        axs[2].set_ylim(0)
        axs[2].set_yticks(axs[2].get_yticks())
        axs[2].set_yticklabels([f'{label / 1e6}' for label in axs[2].get_yticks()])
        axs[2].set_ylabel('uploaded video in channel (million)')

        axs[2].set_xlim(left=0)
        axs[2].set_xticks(axs[2].get_xticks())
        axs[2].set_xticklabels([f'{label / 1e6}' for label in axs[2].get_xticks()])
        axs[2].set_xlabel('average_monthly_earning (million)')

        self.controller.show_graph(fig)

    def second_story(self, event):
        year = self.youtube_data['created_year'].unique()
        year = sorted(year)

        result = []
        for i, y in enumerate(year):
            group_year = self.youtube_data[self.youtube_data['created_year'] == y]
            category_counts = group_year['category'].value_counts()
            max_category = category_counts.idxmax()
            max_category_value = category_counts.values.max()
            m = {'Year': y, 'Category': max_category, 'total_created': max_category_value}
            result.append(m)
        year_trend = pd.DataFrame(result)
        year_trend['Year'] = year_trend['Year'].astype(int)

        # bar graph
        fig, ax = plt.subplots(figsize=(15, 5))
        sns.set_style('darkgrid')
        sns.barplot(x='Year', y='total_created', hue='Category', data=year_trend, palette='magma')
        # self.view.display_graph(fig, self.view.story_canvas)
        self.controller.show_graph(fig)

    def third_story(self, event):
        def remove_outliers(df):
            q1 = df.quantile(0.25)
            q3 = df.quantile(0.75)
            iqr = q3 - q1
            lower_bound = q1 - 1.5 * iqr
            upper_bound = q3 + 1.5 * iqr
            return df[(df >= lower_bound) & (df <= upper_bound)]

        # remove outliers for each channel type
        df_no_outliers = self.youtube_data.groupby('category')['average_monthly_earnings'].apply(remove_outliers).reset_index()
        fig, axs = plt.subplots(1, 2, figsize=(13, 5))
        sns.set_style('darkgrid')

        # First subplot (boxplot)
        ax = sns.boxplot(x='average_monthly_earnings', y='category', data=df_no_outliers,
                         hue='category', palette='RdPu', ax=axs[0])
        ax.set_xlim(left=0)
        ax.set_xticks(ax.get_xticks())
        ax.set_xticklabels([f'{int(label / 1e6)}' for label in ax.get_xticks()])
        ax.set_xlabel('average_monthly_earning (million)')
        ax.set_title('Boxplot')

        # Second subplot (histogram)
        sns.histplot(df_no_outliers['average_monthly_earnings'], ax=axs[1], color='skyblue', kde=True)
        axs[1].set_xlabel('average_monthly_earnings')
        axs[1].set_ylabel('Frequency')
        axs[1].set_title('Histogram')

        plt.tight_layout()
        # self.view.display_graph(fig, self.view.story_canvas)
        self.controller.show_graph(fig)

    def create_histogram(self, attribute):
        fig, ax = plt.subplots(figsize=(5, 4))
        to_create = self.youtube_data[attribute]
        to_create.hist()
        for num in ax.get_xticks():
            if num > 1e6:
                ax.set_xlim(left=0)
                ax.set_xticks(ax.get_xticks())
                ax.set_xticklabels(f'{int(num / 1e6)}' for num in ax.get_xticks())
        ax.set_xlabel(f'{attribute} (million)')
        ax.set_ylabel('Frequency')
        ax.set_title(f'Histogram of {attribute}')
        self.controller.show_create_graph(fig)

    def create_scatter(self, attribute_1, attribute_2):
        print(attribute_1, attribute_2)
        if attribute_1 is not None and attribute_2 is not None:
            fig, ax = plt.subplots(figsize=(6, 4))
            sns.set_style('darkgrid')
            sns.regplot(data=self.youtube_data, x=attribute_1, y=attribute_2,
                        line_kws={'color': 'red'}, ax=ax)

            if max(ax.get_yticks()) > 1e6:
                ax.set_ylim(0)
                ax.set_yticks(ax.get_yticks())
                new_ytick_labels = [f'{int(label / 1e6)}' for label in ax.get_yticks()]
                ax.set_yticklabels(new_ytick_labels)
                ax.set_ylabel(f'{attribute_1} (million)')

            if max(ax.get_xticks()) > 1e6:
                ax.set_xlim(left=0)
                ax.set_xticks(ax.get_xticks())
                new_xtick_labels = [f'{int(label / 1e6)}' for label in ax.get_xticks()]
                ax.set_xticklabels(new_xtick_labels)
                ax.set_xlabel(f'{attribute_2} (million)')

            ax.set_title(f'Correlation between {attribute_1} and {attribute_2}')
            return self.controller.show_create_graph(fig)

