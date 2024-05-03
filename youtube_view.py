import tkinter as tk
from tkinter import *
from tkinter import ttk
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg


class YouTubeView(tk.Tk):
    def __init__(self, controller):
        super().__init__()
        self.title('YouTube Trend Analysis')
        self.configure(bg='#f8f6f2')
        # self.state('zoomed')
        self.controller = controller
        self.canvas = None
        self.fig = None
        self.check_menu = None
        # self.model = YouTubeModel(self)
        self.init_component()

    def init_component(self):
        # Create top frame and menu
        self.top_frame = Frame(self, bg='#f8f6f2', height=130, highlightbackground='#cd3c3c', highlightthickness=4)
        self.top_frame.pack(side=tk.TOP, fill=tk.X)
        self.menu_page = Frame(self, bg='#f1e8d7')
        self.menu_page.pack(side=tk.LEFT, anchor='w', fill=tk.Y, expand=True)
        self.name = tk.Label(self.top_frame, text='YouTube Trend Analysis', font=('Bodoni 72 Oldstyle', 70),
                             fg='#cd3c3c', bg='#f8f6f2')
        self.name.pack(fill=tk.X, expand=True)
        # self.menu_page = Frame(self, height=300, width=230, bg='#cd3c3c')
        self.home_button = tk.Button(self.menu_page, text='Home', font=('Bodoni 72 Oldstyle', 20), bd=0,
                                     fg='#cd3c3c', width=10)
        self.home_button.pack(side=tk.TOP, padx=10, pady=40)

        self.story_button = tk.Button(self.menu_page, text='Story Telling', font=('Bodoni 72 Oldstyle', 20),
                                      bd=0, fg='#cd3c3c', width=10)
        self.story_button.pack(side=tk.TOP, padx=10, pady=40)

        self.create_button = tk.Button(self.menu_page, text='Create Graph', font=('Bodoni 72 Oldstyle', 20),
                                      bd=0, fg='#cd3c3c', width=10)
        self.create_button.pack(side=tk.TOP, padx=15, pady=40)

        self.exit_button = tk.Button(self.menu_page, text='Exit', font=('Bodoni 72 Oldstyle', 20),
                                      bd=0, fg='#cd3c3c', width=10)
        self.exit_button.pack(side=tk.BOTTOM, padx=10, pady=40)
        self.show_menu = Frame(self, bg='#f8f6f2', width=900)
        self.create_story_page()
        self.create_menu_graph_page()

    def create_story_page(self):
        self.story_frame = Frame(self.show_menu, bg='#f8f6f2', width=900)
        self.story_menu_frame = Frame(self.story_frame, bg='#cd3c3c', height=80)
        self.story_menu_frame.pack(side=tk.TOP, fill=tk.BOTH, expand=True)
        self.show_graph_frame = Frame(self.story_frame, bg='#f8f6f2', width=200, height=700)
        self.show_graph_frame.pack(side=tk.TOP, fill=tk.BOTH, expand=True)
        self.tree_frame = Frame(self.show_graph_frame, width=650, height=680)
        self.create_table()
        self.story_canvas = tk.Canvas(self.show_graph_frame, bg='red', width=400, height=400)
        self.story_canvas.pack(side=tk.TOP, anchor='w', fill=tk.BOTH, expand=True)
        self.corr_button = tk.Button(self.story_menu_frame, text='Correlation', width=15, height=1,
                                     font=('Bodoni 72 Oldstyle', 20), bd=0, fg='#cd3c3c')
        self.corr_button.pack(side=tk.LEFT, fill=tk.X, expand=True, padx=52, pady=5)
        self.year_trend_button = tk.Button(self.story_menu_frame, text='Year Trend', width=15, height=1,
                                           font=('Bodoni 72 Oldstyle', 20), bd=0, fg='#cd3c3c')
        self.year_trend_button.pack(side=tk.LEFT, fill=tk.X, expand=True, padx=52, pady=5)
        self.avg_earning_button = tk.Button(self.story_menu_frame, text='Average Earning', width=15, height=1,
                                            font=('Bodoni 72 Oldstyle', 20), bd=0, fg='#cd3c3c')
        self.avg_earning_button.pack(side=tk.LEFT, fill=tk.X, expand=True, padx=52, pady=5)
        self.descriptive_button = tk.Button(self.story_menu_frame, text='Descriptive', width=15, height=1,
                                            font=('Bodoni 72 Oldstyle', 20), bd=0, fg='#cd3c3c')
        self.descriptive_button.pack(side=tk.LEFT, fill=tk.X, expand=True, padx=52, pady=5)

    def show_story_page(self):
        self.clear_menu()
        self.story_frame.pack(side=tk.TOP, anchor='w', fill=tk.BOTH, expand=True)
        self.show_menu.pack(side=tk.TOP, anchor='w', fill=tk.BOTH, expand=True)

    def create_menu_graph_page(self):
        # self.create_graph_frame = Frame(self.show_menu, bg='#f8f6f2')
        # self.create_graph_frame.pack(side=tk.TOP, anchor='w', fill=tk.BOTH, expand=True)
        # self.select_type_frame = Frame(self.create_graph_frame, bg='#f8f6f2')
        self.select_type_frame = Frame(self.show_menu, bg='#f8f6f2')
        # self.select_type_frame.pack(side=tk.LEFT, anchor='w', fill=tk.X, expand=True)
        self.select_first_row = Frame(self.select_type_frame, bg='#f8f6f2')
        self.select_first_row.pack(side=tk.TOP, fill=tk.X, expand=True, padx=0)
        self.select_second_row = Frame(self.select_type_frame, bg='#f8f6f2')
        self.select_second_row.pack(side=tk.TOP, fill=tk.X, expand=True, padx=0)
        self.create_graph_canvas = tk.Canvas(self.select_type_frame, bg='red', width=400, height=400)
        self.create_graph_canvas.pack(side=tk.BOTTOM, anchor='w', fill=tk.BOTH, expand=True)

        self.hist_icon = tk.PhotoImage(file='histogram_icon.png')
        self.hist_button = tk.Button(self.select_first_row, image=self.hist_icon)
        self.hist_button.pack(side=tk.LEFT, expand=True)
        self.hist_label = tk.Label(self.select_first_row, text='Histogram', bg='#cd3c3c', fg='#f8f6f2',
                                   font=('Bodoni 72 Oldstyle', 22), width=30, height=2)
        self.hist_label.pack(side=tk.LEFT, fill=tk.X, expand=True, padx=30)

        self.scatter_icon = tk.PhotoImage(file='scatter_icon.png')
        self.scatter_button = tk.Button(self.select_first_row, image=self.scatter_icon)
        self.scatter_button.pack(side=tk.LEFT, expand=True)
        self.scatter_label = tk.Label(self.select_first_row, text='Scatter Graph', bg='#cd3c3c', fg='#f8f6f2',
                                      font=('Bodoni 72 Oldstyle', 22), width=30, height=2)
        self.scatter_label.pack(side=tk.LEFT, fill=tk.X, expand=True, padx=30)

        self.pie_icon = tk.PhotoImage(file='pie_icon.png')
        self.pie_button = tk.Button(self.select_second_row, image=self.pie_icon)
        self.pie_button.pack(side=tk.LEFT, expand=True)
        self.pie_label = tk.Label(self.select_second_row, text='Pie Chart', bg='#cd3c3c', fg='#f8f6f2',
                                  font=('Bodoni 72 Oldstyle', 22), width=30, height=2)
        self.pie_label.pack(side=tk.LEFT, fill=tk.X, expand=True, padx=30)

        self.bar_icon = tk.PhotoImage(file='bar_icon.png')
        self.bar_button = tk.Button(self.select_second_row, image=self.bar_icon)
        self.bar_button.pack(side=tk.LEFT, expand=True)
        self.bar_label = tk.Label(self.select_second_row, text='Bar Graph', bg='#cd3c3c', fg='#f8f6f2',
                                  font=('Bodoni 72 Oldstyle', 22), width=30, height=2)
        self.bar_label.pack(side=tk.LEFT, fill=tk.X, expand=True, padx=30)

        self.hist_selected()
        self.bar_selected()
        self.scatter_selected()
        self.pie_selected()

    def hist_selected(self):
        self.show_hist_frame = Frame(self.select_type_frame, bg='#f8f6f2')
        self.select_hist_label = tk.Label(self.show_hist_frame, text='Select attribute to see histogram',
                                          font=('Bodoni 72 Oldstyle', 22), bg='#f8f6f2')
        self.select_hist_label.pack(side=tk.LEFT)
        self.select_hist_att = ttk.Combobox(self.show_hist_frame, state='readonly', width=30)
        self.select_hist_att['values'] = ['Subscribers', 'Video views', 'Uploaded videos', 'Average monthly earnings']
        self.select_hist_att.pack(side=tk.LEFT)
        # self.create_graph_canvas.pack(side=tk.TOP, anchor='w', fill=tk.BOTH, expand=True)

    def scatter_selected(self):
        self.show_scatter_frame = Frame(self.select_type_frame, bg='#f8f6f2')
        self.select_scatter_label = tk.Label(self.show_scatter_frame, text='Select attribute to see scatter graph',
                                          font=('Bodoni 72 Oldstyle', 22), bg='#f8f6f2')
        self.select_scatter_label.pack(side=tk.LEFT)
        self.select_scatter_att_1 = ttk.Combobox(self.show_scatter_frame, width=20, state='readonly')
        self.select_scatter_att_1['values'] = ['Subscribers', 'Video views', 'uploaded videos',
                                               'Average monthly earnings']
        self.select_scatter_att_1.pack(side=tk.LEFT)
        self.select_scatter_att_2 = ttk.Combobox(self.show_scatter_frame, width=20, state='readonly')
        self.select_scatter_att_2['values'] = ['Subscribers', 'Video views', 'Uploaded videos',
                                               'Average monthly earnings']
        self.select_scatter_att_2.pack(side=tk.LEFT)

    def pie_selected(self):
        self.show_pie_frame = Frame(self.select_type_frame, bg='#f8f6f2')
        self.select_pie_label = tk.Label(self.show_pie_frame, text='Select attribute to see pie chart',
                                          font=('Bodoni 72 Oldstyle', 22), bg='red')
        self.select_pie_label.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)
        self.select_pie_att = ttk.Combobox(self.show_pie_frame, width=20, state='readonly')
        self.select_pie_att['values'] = ['Subscribers', 'Video views', 'Uploaded videos', 'Average monthly earnings']
        self.select_pie_att.pack(side=tk.TOP, expand=True)

    def bar_selected(self):
        self.show_bar_frame = Frame(self.select_type_frame, bg='#f8f6f2')
        self.select_bar_label = tk.Label(self.show_bar_frame, text='Select attribute to see bar graph',
                                          font=('Bodoni 72 Oldstyle', 22), bg='red')
        self.select_bar_label.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)
        self.select_bar_att = ttk.Combobox(self.show_bar_frame, width=20, state='readonly')
        self.select_bar_att['values'] = ['Subscribers', 'Video views', 'Uploaded videos', 'Average monthly earnings']
        self.select_bar_att.pack(side=tk.TOP, expand=True)

    def show_create_graph_page(self, num, event):
        self.clear_menu()
        self.clear_previous()
        self.select_type_frame.pack(side=tk.TOP, anchor='w', fill=tk.X, expand=True)
        self.show_menu.pack(side=tk.LEFT, anchor='w', fill=tk.BOTH, expand=True)
        if num == 1:
            self.clear_menu()
            self.show_create_hist()
            self.check_menu = 'histogram'
        elif num == 2:
            self.clear_menu()
            self.show_create_scatter()
            self.check_menu = 'scatter'
        elif num == 3:
            self.clear_menu()
            self.show_create_pie()
            self.check_menu = 'pie'
        elif num == 4:
            self.clear_menu()
            self.show_create_bar()
            self.check_menu = 'bar'

    def clear_previous(self):
        if self.check_menu == 'histogram':
            self.show_hist_frame.pack_forget()
        elif self.check_menu == 'scatter':
            self.show_scatter_frame.pack_forget()
        elif self.check_menu == 'pie':
            self.show_pie_frame.pack_forget()
        elif self.check_menu == 'bar':
            self.show_bar_frame.pack_forget()

    def show_create_hist(self):
        self.select_type_frame.pack(side=tk.TOP, anchor='w', fill=tk.X, expand=True)
        self.show_hist_frame.pack(side=tk.TOP, anchor='w', fill=tk.BOTH, expand=True)
        self.create_graph_canvas.pack(side=tk.TOP, anchor='w', fill=tk.BOTH, expand=True)
        self.show_menu.pack(side=tk.LEFT, anchor='w', fill=tk.BOTH, expand=True)

    def show_create_scatter(self):
        self.select_type_frame.pack(side=tk.TOP, anchor='w', fill=tk.X, expand=True)
        self.show_scatter_frame.pack(side=tk.TOP, anchor='w', fill=tk.BOTH, expand=True)
        self.show_menu.pack(side=tk.LEFT, anchor='w', fill=tk.BOTH, expand=True)

    def show_create_pie(self):
        self.select_type_frame.pack(side=tk.TOP, anchor='w', fill=tk.X, expand=True)
        self.show_pie_frame.pack(side=tk.TOP, anchor='w', fill=tk.BOTH, expand=True)
        self.show_menu.pack(side=tk.LEFT, anchor='w', fill=tk.BOTH, expand=True)

    def show_create_bar(self):
        self.select_type_frame.pack(side=tk.TOP, anchor='w', fill=tk.X, expand=True)
        self.show_bar_frame.pack(side=tk.TOP, anchor='w', fill=tk.BOTH, expand=True)
        self.show_menu.pack(side=tk.LEFT, anchor='w', fill=tk.BOTH, expand=True)

    def display_graph(self, fig, graph):
        # Clear any existing graph on the canvas
        if self.canvas:
            self.canvas.get_tk_widget().destroy()

        # Embed the figure in the canvas
        self.canvas = FigureCanvasTkAgg(fig, master=graph)

        # Draw the canvas
        self.canvas.draw()

        # Pack the canvas onto the frame
        self.canvas.get_tk_widget().pack(side=tk.TOP, fill=tk.BOTH, expand=1)

    def clear_menu(self):
        for w in self.show_menu.winfo_children():
            w.pack_forget()

    def create_table(self):
        # self.story_canvas.pack_forget()
        # self.tree_frame = Frame(self.show_graph_frame, width=650, height=680)
        df = self.controller.get_data()
        df_to_describe = df[['subscribers', 'video views', 'uploads', 'average_monthly_earnings']]
        summary_stats = df_to_describe.describe(percentiles=[.25, .50, .75])
        mean = summary_stats.loc['mean']
        std = summary_stats.loc['std']
        min_val = summary_stats.loc['min']
        max_val = summary_stats.loc['max']

        # Create a custom ttk style
        style = ttk.Style(self.tree_frame)

        # Configure the style to change the background color
        style.configure("Custom.Treeview", background="lightblue", fieldbackground="lightblue")

        # Create TreeView widget
        tree = ttk.Treeview(self.tree_frame, height=7, style="Custom.Treeview")
        tree['columns'] = ['Statistic'] + df_to_describe.columns.tolist()
        tree['show'] = 'headings'

        # Add headings to TreeView
        tree.heading('Statistic', text='Statistic')
        for column in df_to_describe.columns:
            tree.heading(column, text=column)
        tree.column('Statistic', width=55)
        # Add data to TreeView
        tree.insert("", "end", values=['mean'] + mean.tolist())
        tree.insert("", "end", values=[''])
        tree.insert("", "end", values=['std'] + std.tolist())
        tree.insert("", "end", values=[''])
        tree.insert("", "end", values=['min'] + min_val.tolist())
        tree.insert("", "end", values=[''])
        tree.insert("", "end", values=['max'] + max_val.tolist())

        tree.pack()
        # self.tree_frame.pack()

    def show_table(self):
        self.tree_frame.pack()

    def bind(self, sequence=None, func=None, add=None):
        for w in self.winfo_children():
            w.bind(sequence, func)
