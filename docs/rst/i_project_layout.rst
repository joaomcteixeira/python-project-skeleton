Project Layout                                                                  
--------------                                                                  
                                                                                
The project layout follows the ``src``, ``tests``, ``docs`` and ``devtools`` folders layout.
                                                                                
The src layout                                                                  
~~~~~~~~~~~~~~                                                                  
                                                                                
I have discovered that storing the source library folder under a ``src`` directory instead of directly in the project's root is by far the most controversial point out there on the wild Internet. Here I adopted the ``src``-based layout discussed by `ionel`_ in his `blog post`_. When reading through the discussed arguments, I found this strategy to have many advantages over the common root directory layout and no added disadvantage.
                                                                                
In detail, though encapsulating the source in a ``src`` directory is an uncommon practice in Python projects, adopting this practice avoids unexpected and uncontrolled code imports that could lead to wrong testing operations, as well stated by `ionel`_, see his `src-nosrc example`_. On the same hand, encapsulating the source under a ``src`` directory does not create any additional problems that would be avoided by the *standard* layout with source directly on a rootdir-based folder, usually named the same as the package name.
                                                                                
tests                                                                           
~~~~~                                                                           
                                                                                
Tests are nicely encapsulated in a ``tests`` folder. With this encapsulation, outside the library folder, it is easier to control that tests do not import from relative paths and can only access the library code after library installation (whatever the installation mode is). Also, having ``tests`` in a separated folder facilitates the configuration files layout on excluding tests from deployment (``MANIFEST.in``) and code quality (``.codacy.yaml``) or coverage (``.coveragerc``). 
                                                                                
docs                                                                            
~~~~                                                                            
                                                                                
All documentation related files are stored in a ``docs`` folder. These include files related to the library documentation but also with the development process, such as: ``AUTHORS``, ``CONTRIBUTING``, ``CHANGELOG``, etc.
                                                                                
devtools                                                                        
~~~~~~~~                                                                        
                                                                                
The ``devtools`` folder hosts the files related to development. Here I used the idea explained by `Chodera Lab`_ in their `structuring your project`_ guidelines, though for other issues described previously, I do not follow their guides, as explained in context.

.. _ionel: https://github.com/ionelmc
.. _blog post: https://blog.ionelmc.ro/2014/05/25/python-packaging/
.. _src-nosrc example: https://github.com/ionelmc/python-packaging-blunders
.. _Chodera lab: https://github.com/choderalab
.. _structuring your project: https://github.com/choderalab/software-development/blob/master/STRUCTURING_YOUR_PROJECT.md
