from youtube_view import YouTubeView
from data_manage import StoryTelling
import tkinter as tk


class YouTubeController:
    def __init__(self):
        self.story = StoryTelling(self)
        self.view = YouTubeView(self)
        # self.model = model
        self.scatter_attribute_1 = None
        self.scatter_attribute_2 = None
        self.bind_button()

    def bind_button(self):
        self.view.home_button.bind('<Button-1>', lambda event: self.handle_menu(2))
        self.view.story_button.bind('<Button-1>', lambda event: self.handle_menu(1))
        self.view.create_button.bind('<Button-1>', lambda event: self.handle_menu(5))

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

    def handle_menu(self, num):
        if num == 1:
            self.view.story_canvas.pack(side=tk.TOP, anchor='w', fill=tk.BOTH, expand=True)
            self.story_and_default()
        elif num == 2:
            self.view.show_home_page()
        elif num == 5:
            self.create_and_default(num)

    def story_and_default(self):
        self.view.table_frame.pack_forget()
        self.view.show_story_page()
        self.story.first_story(event=None)

    def create_and_default(self, num):
        self.story.create_histogram('subscribers')
        self.view.show_create_graph_page(num, event=None)

    def show_first_graph(self):
        self.story.first_story(event=None)

    def show_second_graph(self):
        self.story.second_story(event=None)

    def show_third_graph(self):
        self.story.third_story(event=None)

    def handle_story_page(self, num):
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
        self.view.display_graph(fig, self.view.story_canvas)

    def show_create_graph(self, fig):
        self.view.display_graph(fig, self.view.create_graph_canvas)

    def get_data(self):
        return self.story.youtube_data

    def handle_create_graph(self, num):
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
        attribute = self.view.select_hist_att.get()
        if attribute == 'Subscribers':
            self.story.create_histogram('subscribers')
        elif attribute == 'Video views':
            self.story.create_histogram('video views')
        elif attribute == 'Uploaded videos':
            self.story.create_histogram('uploads')
        elif attribute == 'Average monthly earnings':
            self.story.create_histogram('average_monthly_earnings')

    def handle_scatter_att_1(self):
        attribute_1 = self.view.select_scatter_att_1.get()
        if attribute_1 == 'Subscribers':
            return 'subscribers'
        elif attribute_1 == 'Video views':
            return 'video views'
        elif attribute_1 == 'Uploaded videos':
            return 'uploads'
        elif attribute_1 == 'Average monthly earnings':
            return 'average_monthly_earnings'

    def handle_scatter_att_2(self):
        attribute_2 = self.view.select_scatter_att_2.get()
        if attribute_2 == 'Subscribers':
            return 'subscribers'
        elif attribute_2 == 'Video views':
            return 'video views'
        elif attribute_2 == 'Uploaded videos':
            return 'uploads'
        elif attribute_2 == 'Average monthly earnings':
            return 'average_monthly_earnings'

    def handle_create_scatter(self, event):
        self.scatter_attribute_1 = self.handle_scatter_att_1()
        self.scatter_attribute_2 = self.handle_scatter_att_2()
        if (self.scatter_attribute_1 is not None and self.scatter_attribute_2 is not None
                and self.view.select_scatter_att_1.get() and self.view.select_scatter_att_2.get()):
            self.story.create_scatter(self.scatter_attribute_1, self.scatter_attribute_2)

    def handle_create_pie(self, event):
        year = self.view.select_pie_att.get()
        self.story.create_pie(year)

    def handle_create_bar(self, event):
        attribute = self.view.select_bar_att.get()
        if attribute == 'Subscribers':
            self.story.create_bar('subscribers')
        elif attribute == 'Video views':
            self.story.create_bar('video views')
        elif attribute == 'Uploaded videos':
            self.story.create_bar('uploads')
        elif attribute == 'Average monthly earnings':
            self.story.create_bar('average_monthly_earnings')

    def run(self):
        self.view.mainloop()


