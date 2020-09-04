def age_hist(dataset, pass_class, color=palette[1]):
    hist, edges = np.histogram(dataset[dataset['Pclass'] == int(pass_class)]['Age'].fillna(df['Age'].mean()), bins=25)
    
    source = ColumnDataSource({
        'hist': hist,
        'edges_left': edges[:-1],
        'edges_right': edges[1:]
    })

    hover_tool = HoverTool(
        tooltips=[('From', '@edges_left'), ('Thru', '@edges_right'), ('Count', '@hist')], 
        mode='vline'
    )
    
    p = figure(plot_height=400, title='Age Histogram', tools=[hover_tool])
    p.quad(top='hist', bottom=0, left='edges_left', right='edges_right', source=source,
            fill_color=color, line_color='black')

    plot_styler(p)
    p.sizing_mode = 'scale_width'

    return p