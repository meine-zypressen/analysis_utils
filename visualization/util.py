# Required parameter: dataframe ... the reference pandas dataframe
# Optional parameters: title ... (string) chart title
#                      file  ... (string) path+filename if you want to save image


def half_masked_corr_heatmap(dataframe, cols=None ,title=None, ax=None, **kwargs):
    cols = dataframe.columns if cols is None else cols
    
    if ax is None:
        plt.figure(figsize=(9,9))
        sns.set(font_scale=1)

    corrs = dataframe[cols].corr()
    mask = np.zeros_like(corrs)
    mask[np.triu_indices_from(mask)] = True

    with sns.axes_style("white"):
        sns.heatmap(corrs, mask=mask, annot=True, cmap="coolwarm", vmax=1, vmin=-1, center=0,
        cbar_kws={"orientation": "horizontal"},
        **kwargs)

    if title: plt.title(f'\n{title}\n', fontsize=18)
    plt.xlabel('')    # optional in case you want an x-axis label
    plt.ylabel('')    # optional in case you want a  y-axis label
    plt.show()
    return


# Required parameters: dataframe ... the reference pandas dataframe
#                      target ... (string) column name of the target variable

# Optional parameters: title ... (string) chart title
#                      file  ... (string) path+filename if you want to save image

def corr_to_target(dataframe, target, cols=None ,title=None, ax=None, **kwargs):
    cols = dataframe.columns if cols is None else cols
    
    if ax is None:
        plt.figure(figsize=(4,6))
        sns.set(font_scale=1)
    
    sns.heatmap(dataframe[cols].corr()[[target]].sort_values(target,
                                                ascending=False)[1:],
                annot=True,
                cmap="coolwarm", vmax=1, vmin=-1, center=0,
                cbar_kws={"orientation": "horizontal"},
                **kwargs)
    
    if title: plt.title(f'\n{title}\n', fontsize=18)
    plt.xlabel('')    # optional in case you want an x-axis label
    plt.ylabel('')    # optional in case you want a  y-axis label
    plt.show();
    
    return