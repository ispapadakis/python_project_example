### Adding the comment (# %%) makes what follows a jupyter-like cell
# Click on Run Cell to Get Results in Interactive Window

# %%
banner = "Hello World \N{grinning face with smiling eyes}"
print(banner)
# %%
string_ = (banner+"  ")*2
for i, x in enumerate(string_):
    print(string_[i:i+len(banner)])
# %%
for i, x in enumerate(string_):
    print(" "*i + string_[i:i+7])
# %%
