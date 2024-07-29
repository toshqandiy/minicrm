from django.contrib.auth.decorators import login_required
from rest_framework import views, response, status
from django.shortcuts import render, get_object_or_404, redirect
from .serializers import CustomerSerializer
from .models import Customer
from django.contrib import messages
from .forms import AddClientForm

@login_required
def customers_list(request):
    customers = Customer.objects.all()
    return render(request, 'customer/customers_list.html', {
        'customers': customers
    })

@login_required
def customers_detail(request, pk):
    customer = get_object_or_404(Customer, pk=pk)

    return render(request, 'customer/customers_detail.html', {
        'customer': customer
    })

@login_required
def customers_add(request):
    if request.method == 'POST':
        form = AddClientForm(request.POST)

        if form.is_valid():
            customer = form.save(commit=False)
            customer.save()

            messages.success(request, 'The customer was created.')

            return redirect('customers_list')
    else:
        form = AddClientForm()

    return render(request, 'customer/customers_add.html', {
        'form': form
    })

@login_required
def customers_edit(request, pk):
    customer = get_object_or_404(Customer, pk=pk)

    if request.method == 'POST':
        form = AddClientForm(request.POST, instance=customer)

        if form.is_valid():
            form.save()

            messages.success(request, 'The changes was saved.')

            return redirect('customers_list')

    else:
        form = AddClientForm(instance=customer)

    return render(request, 'customer/customers_edit.html', {
        'form': form
    })

@login_required
def customers_delete(request, pk):
    customer = get_object_or_404(Customer, pk=pk)
    customer.delete()

    messages.success(request, 'The customer was deleted.')

    return redirect('customers_list')


class CustomerListCreateAPIView(views.APIView):
    serializer_class = CustomerSerializer

    def get(self, request):
        queryset = Customer.objects.all()
        serializer = self.serializer_class(queryset, many=True)
        return response.Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request):
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return response.Response(serializer.data, status=status.HTTP_201_CREATED)


class CustomerDetailView(views.APIView):
    serializer_class = CustomerSerializer
    def get(self, request, pk):
        instance = Customer.objects.get(pk=pk)
        serializer = self.serializer_class(instance=instance)
        return response.Response(serializer.data)

    def patch(self, request, pk):
        instance = Customer.objects.get(pk=pk)
        serializer = self.serializer_class(instance, data=request.data, partial=True)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return response.Response(serializer.data)


    def delete(self, request, pk):
        try:
            instance = Customer.objects.get(pk=pk)
            instance.delete()
            return response.Response(status=status.HTTP_204_NO_CONTENT)
        except Customer.DoesNotExist:
            return response.Response({'message': 'customer not found'})