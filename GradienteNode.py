"""
NAME: Gradient Styler
ICON: icon.png
KEYBOARD_SHORTCUT: 
SCOPE:
Create Gradient Color in Vertical Order Nodes

"""

# The following symbols are added when run as a shelf item script:
# exit():      Allows 'error-free' early exit from the script.
# console_print(message, raiseTab=False):
#              Prints the given message to the result area of the largest
#              available Python tab.
#              If raiseTab is passed as True, the tab will be raised to the
#              front in its pane.
#              If no Python tab exists, prints the message to the shell.
# console_clear(raiseTab=False):
#              Clears the result area of the largest available Python tab.
#              If raiseTab is passed as True, the tab will be raised to the
#              front in its pane.


class GradientColorNodes(QtWidgets.QWidget):

    """
    This Class Create a Gradient Color in Vertical Order Nodes
    Katana nodes are dark gray by default with this function we can change the color
    given by the user, the color will be interpolated between the start color and the end color
    """

    def __init__(self):
        super().__init__()

        # Give name to the Window
        self.setWindowTitle("Gradient Styler v.1.0")
        self.setWindowFlags(self.windowFlags() |
                            QtCore.Qt.WindowStaysOnTopHint)

        self.setFixedSize(400, 150)
        self.build_layout()

    def build_layout(self):
        """
        This Function Create the Layout
        """
        lyt = QtWidgets.QVBoxLayout()
        self.setLayout(lyt)

        # Create a Qlaberl to display the image
        image_label = QtWidgets.QLabel()
        pixmap = QtGui.QPixmap(
            "Paste your path /gradient_Styler_v001.png")
        pixmap = pixmap.scaled(
            400, 50, QtCore.Qt.KeepAspectRatio, QtCore.Qt.SmoothTransformation)
        image_label.setPixmap(pixmap)
        image_label.setAlignment(QtCore.Qt.AlignCenter)

        # Agregar el QLabel al layout principal antes del primer HBox
        lyt.addWidget(image_label)

        color_buttons_layout = QtWidgets.QHBoxLayout()

        # Create Second Color Buttom
        self.second_color = QtWidgets.QPushButton("Select First Color")
        self.second_color.clicked.connect(
            lambda: self.select_color(self.second_color))
        color_buttons_layout.addWidget(self.second_color)

        # Create First Color Buttom
        self.first_color = QtWidgets.QPushButton("Select Second Color")
        self.first_color.clicked.connect(
            lambda: self.select_color(self.first_color))
        color_buttons_layout.addWidget(self.first_color)

        # Add Horizontal Layout  to Vertical Layout
        lyt.addLayout(color_buttons_layout)

        options_buttons_layout = QtWidgets.QHBoxLayout()

        # Line Divisor
        divider = QtWidgets.QFrame()
        divider.setFrameShape(QtWidgets.QFrame.HLine)
        divider.setFrameShadow(QtWidgets.QFrame.Sunken)

        # Add Line to Vertical Layout
        lyt.addWidget(divider)

        # Apply Gradient Button
        apply_btn = QtWidgets.QPushButton("Apply Gradient")
        apply_btn.clicked.connect(self.apply_gradient)
        options_buttons_layout.addWidget(apply_btn)

        # Cancel Button
        cancel_btn = QtWidgets.QPushButton("Cancel")
        cancel_btn.clicked.connect(self.close)
        options_buttons_layout.addWidget(cancel_btn)

        # Add Horizontal Layout  to Vertical Layout
        lyt.addLayout(options_buttons_layout)

        # Connect to Url Github
        link_label = QtWidgets.QLabel(
            '<a href="https://github.com/DanteVFX">by DanteVFX</a>')
        link_label.setAlignment(QtCore.Qt.AlignRight | QtCore.Qt.AlignBottom)
        link_label.setOpenExternalLinks(True)
        link_label.setStyleSheet("color: blue; font-size: 10px;")

        lyt.addWidget(link_label)

    def select_color(self, button):
        """
        This Function Select the Color
        """

        color = QtWidgets.QColorDialog.getColor()
        if color.isValid():
            button.setStyleSheet(f"background-color: {color.name()}")
            button.setProperty("selected_color", color)

    def apply_gradient(self):
        """
        This Function Apply the Gradient
        """
        # Get selected colors
        end_color = self.second_color.property("selected_color")
        start_color = self.first_color.property("selected_color")

        # Check if both colors are selected
        if not start_color or not end_color:
            QtWidgets.QMessageBox.warning(
                self, "Error", "Please select both start and end colors.")
            return

        # Get all selected nodes
        selected_nodes = NodegraphAPI.GetAllSelectedNodes()

        # Check if any nodes are selected
        if len(selected_nodes) < 1:
            QtWidgets.QMessageBox.warning(
                self, "Error", "Please select at least one node.")
            return

        # Apply gradient to selected nodes
        if len(selected_nodes) == 1:
            DrawingModule.SetCustomNodeColor(selected_nodes[0],
                                             start_color.redF(),
                                             start_color.greenF(),
                                             start_color.blueF())
        else:
            """
            To normalize the color between start_color and end_color
            I am using the formula (start_color + end_color) / 2
            it makes the color between start_color and end_color
            giving a gradient effect.
            """

            # Sort nodes by their Y positions
            selected_nodes.sort(
                key=lambda node: NodegraphAPI.GetNodePosition(node)[1])
            total_nodes = len(selected_nodes)

            for index, node in enumerate(selected_nodes):
                t = index / (total_nodes - 1)  # Normalized position
                interpolated_color = QtGui.QColor()
                interpolated_color.setRedF(
                    start_color.redF() * (1 - t) + end_color.redF() * t)
                interpolated_color.setGreenF(
                    start_color.greenF() * (1 - t) + end_color.greenF() * t)
                interpolated_color.setBlueF(
                    start_color.blueF() * (1 - t) + end_color.blueF() * t)

                DrawingModule.SetCustomNodeColor(node,
                                                 interpolated_color.redF(),
                                                 interpolated_color.greenF(),
                                                 interpolated_color.blueF())


ui = GradientColorNodes()
ui.show()
