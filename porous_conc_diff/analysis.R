library(np)



# Read CSV 
input <- read.csv(file="/home/qth20/Documents/lammps-sph/lammps-test-case/porous_conc_diff/uq.csv", 
                  header=TRUE, sep=",")

# Set random subset of data
set.seed(123)
ii <- sample(seq(1, nrow(input)), replace=FALSE)

# Generate train and eval
input.train <- input[ii[1:100],]
input.eval <- input[ii[101:nrow(input)],]

DA <- as.matrix(input['DA'])
DB <- as.matrix(input['DB'])
DC <- as.matrix(input['DC'])
k <- as.matrix(input['k'])
cC <- as.matrix(input['cC'])

# OLS model
model.ols <- lm(cC ~ DA + DB + DC + k, 
                data=input.train)
summary(model.ols)
# Fit with OLS model
fit.ols <- predict(model.ols,
                   data=input.train,
                   newdata=input.eval)
# Calculate predicted square error
pse.ols <- mean((input.eval$cC - fit.ols)^2)

# NP model
bw.subset <- npregbw(formula=cC ~ DA + DB + DC + k, 
                  regtype="ll",
                  bwmethod="cv.aic",
                  data=input.train)
model.np <- npreg(bws = bw.subset)
summary(model.np)
# Fit with NP model
fit.np <- predict(model.np,
                  data=input.train,
                  newdata=input.eval)
# Calculate predicted square error
pse.np <- mean((input.eval$cC - fit.np)^2)

# Use full data 
# NP model
bw.full <- npregbw(formula=cC ~ DA + DB + DC + k, 
                     regtype="ll",
                     bwmethod="cv.aic",
                     data=input)
model.np.full <- npreg(bws=bw.full)
# Fit with NP model
fit.np.full <- predict(model.np.full,
                       data=input)
# Calculate error
pse.np.full <- mean((input$cC - fit.np.full)^2)

# Plot the bootstrap
plot(model.np.full, plot.errors.method="bootstrap", plot.errors.boot.num=25)
