# p-tree 0.1.14

## About

```
This package is used to count the CFUs in petri dishes.
In order to use it you must provide it with a shared dropbox link to a directory containing the images in a png format.
Only images must be contained in the directory no subdirectories.
```

# THIS

![alt text](https://raw.githubusercontent.com/gpamfilis/p-tree/master/ORIGINANL.png)

# TO THIS

![alt text](https://raw.githubusercontent.com/gpamfilis/p-tree/master/MODIFIED.png)


# If it misses a few its ok! it gets them by cutting and rotating the original image!

### Installation
```
This package requires python==3.6

to install type:

pip install p-tree

or

pip install --upgrade p-tree
```

### Instuctions

1. Copy the example script bellow and run it.
2. An image will pop-up containing a petri dish with some (or all colonies circled).
3. If not all are circled **close** the image and enter `n` in the `Accept?` message of the prompt.
4. Enter after that the pixel size of the colony (estimate). The x and y axis are numbered.
5. Once the pixel size is added a new image will pop-up.
If satisfied **close** the image and type `y` in the `Accept?` field. If not satisfied go back to **3**.

### Example Script


```python
from p_tree.run import CountColonies

if __name__ == '__main__':
    url = 'https://www.dropbox.com/sh/vq4wb9fd9k1fz49/AADLR3IIgj8lMWs8m9QLzdPoa?dl=1'
    cc = CountColonies(url=url)
    dfs = cc.main()
    print(dfs)
```

# IMPORTANT (for now)

At the end of your dropbox-link it says **?dl=0**. change it to **?dl=1**.

# TODO

1. Provide rotate angle option and number of rotations.
2. Accept directory as input and not only dropbox shared link.
3. Save DataFrames to csv.
4. Output analytics such as bell curves (mean and std) for all petries.
5. modify makefile to pip install reqs.
6. modify makefile to unistall reqs.
7. modify makefile to build and deploy.
8. convert it into a flask extension for www.engineer-it.org.
9. make video on youtube on how to use it.
10. show jupyter notebook example steps.
11. include images
