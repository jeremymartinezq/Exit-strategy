def exit_strategy_analysis(initial_investment, exit_values, years):
    rois = {strategy: (exit_value - initial_investment) / initial_investment / years
            for strategy, exit_value in exit_values.items()}
    return rois


# Example inputs
initial_investment = 100  # in millions
exit_values = {'IPO': 300, 'Sale': 250, 'Merger': 275}  # Exit values in millions
years = 5

rois = exit_strategy_analysis(initial_investment, exit_values, years)
for strategy, roi in rois.items():
    print(f"ROI for {strategy}: {roi * 100:.2f}% per year")


