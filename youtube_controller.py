import tkinter as tk
from youtube_view import YouTubeView
from data_manage import StoryTelling


class YouTubeController:
    """
    The controller object for managing the GUI application.
    """
    def __init__(self):
        """
        Initialize the YouTubeController.
        """
        self.story = StoryTelling(self)
        self.view = YouTubeView(self)
        self.scatter_attribute_1 = None
        self.scatter_attribute_2 = None
        self.bind_button()

    def bind_button(self):
        """
        Bind various buttons and combobox to their respective event handlers.
        :return: None
        """
        self.view.home_button.bind('<Button-1>', lambda event: self.handle_menu(2))
        self.view.story_button.bind('<Button-1>', lambda event: self.handle_menu(1))
        self.view.create_button.bind('<Button-1>', lambda event: self.handle_menu(5))
        self.view.suggest_button.bind('<Button-1>', lambda event: self.handle_menu(3))

        self.view.corr_button.bind('<Button-1>', lambda event: self.handle_story_page(1))
        self.view.year_trend_button.bind('<Button-1>', lambda event: self.handle_story_page(2))
        self.view.avg_earning_button.bind('<Button-1>', lambda event: self.handle_story_page(3))
        self.view.descriptive_button.bind('<Button-1>', lambda event: self.handle_story_page(4))

        self.view.hist_button.bind('<Button-1>', lambda event: self.handle_create_graph(1))
        self.view.scatter_button.bind('<Button-1>', lambda event: self.handle_create_graph(2))
        self.view.pie_button.bind('<Button-1>', lambda event: self.handle_create_graph(3))
        self.view.bar_button.bind('<Button-1>', lambda event: self.handle_create_graph(4))

        self.view.select_hist_att.bind('<<ComboboxSelected>>', self.handle_create_hist)
        self.view.select_scatter_att_1.bind('<<ComboboxSelected>>', self.handle_create_scatter)
        self.view.select_scatter_att_2.bind('<<ComboboxSelected>>', self.handle_create_scatter)
        self.view.select_pie_att.bind('<<ComboboxSelected>>', self.handle_create_pie)
        self.view.select_bar_att.bind('<<ComboboxSelected>>', self.handle_create_bar)

        self.view.select_suggest_att.bind('<<ComboboxSelected>>', self.handle_suggest_graph)
        self.view.from_sub.bind('<Button-1>', lambda event: self.handle_suggest_graph(1))
        self.view.from_view.bind('<Button-1>', lambda event: self.handle_suggest_graph(2))

    def handle_menu(self, num):
        """
        Handle displays the menu based on the user-selected option.
        :param num: The number representing the menu selection.
        :return: None
        """
        if num == 1:
            self.view.story_canvas.pack(side=tk.TOP, anchor='w', fill=tk.BOTH, expand=True)
            self.story_and_default()
        elif num == 2:
            self.view.show_home_page()
        elif num == 3:
            self.suggest_and_default()
        elif num == 5:
            self.create_and_default(num)

    def story_and_default(self):
        """
        Handle display 'story telling' menu with default graph.
        :return: None
        """
        self.view.table_frame.pack_forget()
        self.view.show_story_page()
        self.story.default_story_graph()

    def create_and_default(self, num):
        """
        Handle display 'create graph' menu with default graph.
        :param num: The number represent type of graph that user selected.
        :return: None
        """
        self.story.create_histogram('subscribers')
        self.view.show_create_graph_page(num, event=None)

    def suggest_and_default(self):
        """
        Handle display 'suggest channel' menu with default graph.
        :return: None
        """
        self.story.create_suggest_bar_sub('Music')
        self.view.show_suggest_page()

    def show_first_graph(self):
        """
        Create first graph of story telling.
        :return: None
        """
        self.story.first_story(event=None)

    def show_second_graph(self):
        """
        Create second graph of story telling.
        :return: None
        """
        self.story.second_story(event=None)

    def show_third_graph(self):
        """
        Create third graph of story telling.
        :return: None
        """
        self.story.third_story(event=None)

    def handle_story_page(self, num):
        """
        Handle display story pages based on the provided number.
        :param num: The number represent graph that user select.
        :return: None
        """
        if num == 1:
            self.view.table_frame.pack_forget()
            self.view.story_canvas.pack(side=tk.TOP, anchor='w', fill=tk.BOTH, expand=True)
            self.show_first_graph()
        elif num == 2:
            self.view.table_frame.pack_forget()
            self.view.story_canvas.pack(side=tk.TOP, anchor='w', fill=tk.BOTH, expand=True)
            self.show_second_graph()
        elif num == 3:
            self.view.table_frame.pack_forget()
            self.view.story_canvas.pack(side=tk.TOP, anchor='w', fill=tk.BOTH, expand=True)
            self.show_third_graph()
        elif num == 4:
            self.view.story_canvas.pack_forget()
            self.view.show_table()

    def show_graph(self, fig):
        """
        Handle display graph in 'story telling' menu.
        :param fig: The matplotlib figure object.
        :return: None
        """
        self.view.display_graph(fig, self.view.story_canvas)

    def show_create_graph(self, fig):
        """
        Handle display graph in 'create graph' page.
        :param fig: The matplotlib figure object.
        :return: None
        """
        self.view.display_graph(fig, self.view.create_graph_canvas)

    def show_suggest_graph(self, fig):
        """
        Handle display graph in 'suggest channel' menu
        :param fig: The matplotlib figure object.
        :return: None
        """
        self.view.display_graph(fig, self.view.suggest_canvas)

    def get_data(self):
        """
        Get data from dataset.
        :return: None
        """
        return self.story.youtube_data

    def get_unique_category(self):
        """
        Get unique category from dataset.
        :return: None
        """
        unique_category = list(self.story.youtube_data['category'].unique())
        return unique_category

    def handle_create_graph(self, num):
        """
        Handle display create graph base on the provide number.
        :param num: The number represent type of graph that user select.
        :return: None
        """
        if num == 1:
            self.story.create_histogram('subscribers')
        elif num == 2:
            self.story.create_scatter('subscribers', 'video views')
        elif num == 3:
            self.story.create_pie('2005')
        elif num == 4:
            self.story.create_bar('subscribers')
        self.view.show_create_graph_page(num, event=None)

    def handle_create_hist(self, event):
        """
        Handle create histogram based on selected attribute.
        :return: None
        """
        attribute = self.view.select_hist_att.get()
        if attribute == 'Subscribers':
            self.story.create_histogram('subscribers')
        elif attribute == 'Video views':
            self.story.create_histogram('video views')
        elif attribute == 'Average monthly earnings':
            self.story.create_histogram('average_monthly_earnings')

    def handle_scatter_att_1(self):
        """
        Handle attribute from combobox.
        :return: attribute that user select to create graph.
        """
        attribute_1 = self.view.select_scatter_att_1.get()
        if attribute_1 == 'Subscribers':
            return 'subscribers'
        if attribute_1 == 'Video views':
            return 'video views'
        if attribute_1 == 'Uploaded videos':
            return 'uploads'
        if attribute_1 == 'Average monthly earnings':
            return 'average_monthly_earnings'

    def handle_scatter_att_2(self):
        """
        Handle attribute from combobox.
        :return: attribute that user select to create graph.
        """
        attribute_2 = self.view.select_scatter_att_2.get()
        if attribute_2 == 'Subscribers':
            return 'subscribers'
        if attribute_2 == 'Video views':
            return 'video views'
        if attribute_2 == 'Uploaded videos':
            return 'uploads'
        if attribute_2 == 'Average monthly earnings':
            return 'average_monthly_earnings'

    def handle_create_scatter(self, event):
        """
        Handle create scatter graph based on selected attribute.
        :return: None
        """
        self.scatter_attribute_1 = self.handle_scatter_att_1()
        self.scatter_attribute_2 = self.handle_scatter_att_2()
        if (self.scatter_attribute_1 is not None and self.scatter_attribute_2 is not None
                and self.view.select_scatter_att_1.get() and self.view.select_scatter_att_2.get()):
            self.story.create_scatter(self.scatter_attribute_1, self.scatter_attribute_2)

    def handle_create_pie(self, event):
        """
        Handle create pie chart based on selected attribute.
        :return: None
        """
        year = self.view.select_pie_att.get()
        self.story.create_pie(year)

    def handle_create_bar(self, event):
        """
        Handle create bar graph based on selected attribute.
        :return: None
        """
        attribute = self.view.select_bar_att.get()
        if attribute == 'Subscribers':
            self.story.create_bar('subscribers')
        elif attribute == 'Video views':
            self.story.create_bar('video views')
        elif attribute == 'Uploaded videos':
            self.story.create_bar('uploads')
        elif attribute == 'Average monthly earnings':
            self.story.create_bar('average_monthly_earnings')

    def handle_suggest_graph(self, num):
        """
        Handle 'suggest channel' menu.
        :param num: The number represent attribute that user select.
        :return: None
        """
        category = self.view.select_suggest_att.get()
        if category is not None and num == 1:
            self.story.create_suggest_bar_sub(category)
        if category is not None and num == 2:
            self.story.create_suggest_bar_view(category)

    def run(self):
        """
        Run application.
        :return: None
        """
        self.view.mainloop()

