import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
from smt.surrogate_models import KRG

data = pd.read_csv("Info_To_HEEDS.csv") #Change this name for the path to the csv file imported by the main function
xt = data.loc[:,'Breakdown Pressure (psi)'].values
yt = data.loc[:,'Final ISIP (psi)'].values

sm = KRG(theta0=[1e-2])
sm.set_training_values(xt, yt)
sm.train()

num = 100
x = np.linspace(4000, 6600, num)
y = sm.predict_values(x)
# estimated variance
s2 = sm.predict_variances(x)
# derivative according to the first variable
dydx = sm.predict_derivatives(xt, 0)
fig, axs = plt.subplots(1)

# add a plot with variance
axs.plot(xt, yt, "o")
axs.plot(x, y)
axs.fill_between(
    np.ravel(x),
    np.ravel(y - 3 * np.sqrt(s2)),
    np.ravel(y + 3 * np.sqrt(s2)),
    color="lightgrey",
)
axs.set_xlabel("Breakdown Pressure (psi)")
axs.set_ylabel("Final ISIP (psi)")
axs.legend(
    ["Training data", "Prediction", "Confidence Interval 99%"],
    loc="lower right",
)

plt.show()

